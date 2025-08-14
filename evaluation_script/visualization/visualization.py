import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the CSV
file_path = 'visualization/matrix_multiplication-random.csv'
df = pd.read_csv(file_path)

# Convert timestamp column to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Target timestamp to highlight
event_markers = [
    (pd.to_datetime("2025-07-31T09:31:47.414855"), "Change to GPU"),
]


# Plotting
fig, ax1 = plt.subplots(figsize=(12, 6))

# Left y-axis: response_time_ms
ax1.plot(df['timestamp'], df['response_time_ms'], color='tab:blue', label='Response Time (ms)')
ax1.set_xlabel('Time')
ax1.set_ylabel('Response Time (ms)', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

# # Right y-axis: matrix_size
# ax2 = ax1.twinx()
# ax2.plot(df['timestamp'], df['matrix_size'], color='tab:orange', label='Matrix Size')
# ax2.set_ylabel('Matrix Size', color='tab:orange')
# ax2.tick_params(axis='y', labelcolor='tab:orange')

# Add vertical lines and labels for each event
for ts, label in event_markers:
    ax1.axvline(x=ts, color='red', linestyle='--', linewidth=2)
    ax1.text(ts, ax1.get_ylim()[1] * 0.95, label,
             color='red', rotation=90, verticalalignment='top',
             horizontalalignment='right', fontsize=10)

# Final touches
fig.autofmt_xdate()
# plt.title("Matrix Multiplication (increment): Response Time vs Matrix Size")
fig.tight_layout()

plt.savefig("plot.png", dpi=300, bbox_inches='tight')
plt.show()

