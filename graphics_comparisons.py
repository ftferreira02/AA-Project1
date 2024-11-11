import matplotlib.pyplot as plt
from pandas_transformations import results_df
def plot_execution_time_comparison(df):
    plt.figure(figsize=(12, 6))
    for algorithm in df["Algorithm"].unique():
        subset = df[df["Algorithm"] == algorithm]
        plt.bar(subset["Graph"], subset["Time_Taken"], label=algorithm, alpha=0.7)
    plt.xlabel("Graph")
    plt.ylabel("Time Taken (seconds)")
    plt.title("Execution Time Comparison: Greedy vs. Exhaustive")
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.savefig("Plots/execution_time_comparison.png")
    plt.show()

def plot_basic_operations_comparison(df):
    plt.figure(figsize=(12, 6))
    for algorithm in df["Algorithm"].unique():
        subset = df[df["Algorithm"] == algorithm]
        plt.bar(subset["Graph"], subset["Basic_Operations"], label=algorithm, alpha=0.7)
    plt.xlabel("Graph")
    plt.ylabel("Basic Operations")
    plt.title("Basic Operations Comparison: Greedy vs. Exhaustive")
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.savefig("Plots/basic_operations_comparison.png")
    plt.show()

def plot_solution_quality_comparison(df):
    plt.figure(figsize=(12, 6))
    for algorithm in df["Algorithm"].unique():
        subset = df[df["Algorithm"] == algorithm]
        plt.bar(subset["Graph"], subset["Edge_Dominating_Set_Size"], label=algorithm, alpha=0.7)
    plt.xlabel("Graph")
    plt.ylabel("Edge Dominating Set Size")
    plt.title("Edge Dominating Set Size Comparison: Greedy vs. Exhaustive")
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.savefig("Plots/solution_quality_comparison.png")
    plt.show()

def plot_time_vs_density_comparison(df):
    plt.figure(figsize=(8, 6))
    for algorithm in df["Algorithm"].unique():
        subset = df[df["Algorithm"] == algorithm]
        plt.scatter(subset["Density"], subset["Time_Taken"], label=algorithm, alpha=0.7)
    plt.xlabel("Graph Density")
    plt.ylabel("Time Taken (seconds)")
    plt.title("Execution Time vs. Graph Density: Greedy vs. Exhaustive")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig("Plots/time_vs_density_comparison.png")
    plt.show()

def plot_time_vs_vertices_comparison(df):
    plt.figure(figsize=(8, 6))
    for algorithm in df["Algorithm"].unique():
        subset = df[df["Algorithm"] == algorithm]
        plt.scatter(subset["Vertices"], subset["Time_Taken"], label=algorithm, alpha=0.7)
    plt.xlabel("Number of Vertices")
    plt.ylabel("Time Taken (seconds)")
    plt.title("Execution Time vs. Number of Vertices: Greedy vs. Exhaustive")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig("Plots/time_vs_vertices_comparison.png")
    plt.show()

plot_execution_time_comparison(results_df)
plot_basic_operations_comparison(results_df)
plot_solution_quality_comparison(results_df)
plot_time_vs_density_comparison(results_df)
plot_time_vs_vertices_comparison(results_df)
