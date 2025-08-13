import pandas as pd
import matplotlib.pyplot as plt

# File paths
files = [
    ("matrix_multiplication-increment-4-auto.csv", "Auto"),
    ("matrix_multiplication-increment-4-gpu.csv", "GPU"),
    ("matrix_multiplication-increment-4-cpu.csv", "CPU")
]

# Read and label each dataset
dfs = []
for file, label in files:
    df = pd.read_csv(file)
    df["dataset"] = label
    dfs.append(df)

# Combine all into one DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Plot
plt.figure(figsize=(8, 6))
for label, group in combined_df.groupby("dataset"):
    plt.plot(
        group["matrix_size"],
        group["response_time_ms"],
        marker=",",
        label=label)

plt.xlabel("Matrix Size")
plt.ylabel("Response Time (ms)")
# plt.title("Response Time vs Matrix Size")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("plot.png", dpi=300, bbox_inches='tight')

plt.show()


