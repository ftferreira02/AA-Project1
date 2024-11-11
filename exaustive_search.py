import networkx as nx
import os
import time
import multiprocessing
from itertools import combinations
from graph_utils import parse_graph_from_text, write_result_to_file, visualize_and_save_edge_dominating_set

TIMEOUT = 120  # Timeout in seconds (2 minutes)
GRAPH_TEXT_FILE = "Graphs/all_graphs_data.txt"
RESULT_TEXT_FILE = "Graphs/min_edge_dominating_sets.txt"
MIN_EDGE_DOMINATING_IMG_DIR = "Graphs/ExaustiveSearchImages"

# Ensure the directory exists
os.makedirs(MIN_EDGE_DOMINATING_IMG_DIR, exist_ok=True)

def is_edge_dominating_set(G, edge_subset, edge_coverage):
    for edge in edge_coverage - edge_subset:
        u, v = edge
        if not any(u in e or v in e for e in edge_subset):
            return False
    return True

def minimum_edge_dominating_set_with_timeout(G, timeout=TIMEOUT):
    result_queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=minimum_edge_dominating_set_process, args=(G, result_queue))
    
    start_time = time.time()
    process.start()
    process.join(timeout)
    
    if process.is_alive():
        process.terminate()
        process.join()
        return None, 0, time.time() - start_time, True
    else:
        min_set, operation_count = result_queue.get()
        duration = time.time() - start_time
        return min_set, operation_count, duration, False

def minimum_edge_dominating_set_process(G, result_queue):
    all_edges = list(G.edges())
    all_edges_set = set(all_edges)
    edge_coverage = {edge: set(G.edges(edge[0])).union(G.edges(edge[1])) - {edge} for edge in all_edges}
    
    min_dominating_set = None
    operation_count = 0

    for size in range(1, len(all_edges) + 1):
        for edge_subset in combinations(all_edges, size):
            operation_count += 1
            edge_subset_set = set(edge_subset)
            
            if min_dominating_set and len(edge_subset_set) >= len(min_dominating_set):
                continue
            
            if is_edge_dominating_set(G, edge_subset_set, all_edges_set):
                min_dominating_set = edge_subset_set
                break

        if min_dominating_set:
            break

    result_queue.put((min_dominating_set, operation_count))

def main():
    with open(RESULT_TEXT_FILE, "w") as f:
        f.write("")

    for G, graph_name, num_vertices, density in parse_graph_from_text(GRAPH_TEXT_FILE):
        print(f"Processing {graph_name} with {num_vertices} vertices and density {density}")
        
        min_edge_dominating_set, operation_count, duration, timed_out = minimum_edge_dominating_set_with_timeout(G)
        
        if not timed_out and min_edge_dominating_set:
            visualize_and_save_edge_dominating_set(
                G, min_edge_dominating_set, graph_name, MIN_EDGE_DOMINATING_IMG_DIR,
                title=f"Minimum Edge Dominating Set for {graph_name}", color="red"
            )
        
        write_result_to_file(RESULT_TEXT_FILE, graph_name, min_edge_dominating_set, operation_count, duration, timed_out)

if __name__ == "__main__":
    main()
