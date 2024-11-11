import re
import pandas as pd
import matplotlib.pyplot as plt
import os
from pandas_transformations import greedy_df, exhaustive_df, results_df

# Define a directory to store the plots
PLOT_DIR = "Plots"
os.makedirs(PLOT_DIR, exist_ok=True)  # Ensure the directory exists

# 1. Comparison of Execution Time for each graph
def plot_execution_time(df, search):
    plt.figure(figsize=(12, 6))
    plt.bar(df["Graph"], df["Time_Taken"], color="skyblue")
    plt.xlabel("Graph")
    plt.ylabel("Time Taken (seconds)")
    plt.title("Execution Time for Each Graph")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(os.path.join(PLOT_DIR, f"execution_time_{search}.png"))
  # Save as PNG

# 2. Basic Operations Count
def plot_basic_operations(df, search):
    plt.figure(figsize=(12, 6))
    plt.bar(df["Graph"], df["Basic_Operations"], color="salmon")
    plt.xlabel("Graph")
    plt.ylabel("Basic Operations")
    plt.title("Basic Operations Count for Each Graph")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(os.path.join(PLOT_DIR, f"basic_operations{search}.png"))  # Save as PNG


# 3. Solution Quality Comparison
def plot_solution_quality(df, search):
    plt.figure(figsize=(12, 6))
    plt.bar(df["Graph"], df["Edge_Dominating_Set_Size"], color="lightgreen")
    plt.xlabel("Graph")
    plt.ylabel("Edge Dominating Set Size")
    plt.title("Edge Dominating Set Size for Each Graph")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(os.path.join(PLOT_DIR, f"solution_quality{search}.png"))   # Save as PNG

# 4. Execution Time vs. Graph Density
def plot_time_vs_density(df, search):
    plt.figure(figsize=(8, 6))
    plt.scatter(df["Density"], df["Time_Taken"], color="purple")
    plt.xlabel("Graph Density")
    plt.ylabel("Time Taken (seconds)")
    plt.title("Execution Time vs. Graph Density")
    plt.grid()
    plt.savefig(os.path.join(PLOT_DIR, f"time_vs_density{search}.png"))   # Save as PNG

# 5. Execution Time vs. Number of Vertices
def plot_time_vs_vertices(df, search):
    plt.figure(figsize=(8, 6))
    plt.scatter(df["Vertices"], df["Time_Taken"], color="orange")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Time Taken (seconds)")
    plt.title("Execution Time vs. Number of Vertices")
    plt.grid()
    plt.savefig(os.path.join(PLOT_DIR, f"time_vs_vertices{search}.png"))  # Save as PNG

def generate_graphics_single(df, search):
    plot_execution_time(df , search)
    plot_basic_operations(df, search)
    plot_solution_quality(df, search)
    plot_time_vs_density(df, search)
    plot_time_vs_vertices(df, search)


def main():
    generate_graphics_single(exhaustive_df, "exaustive")
    generate_graphics_single(greedy_df, "greedy")

if __name__ == "__main__":
    main()
