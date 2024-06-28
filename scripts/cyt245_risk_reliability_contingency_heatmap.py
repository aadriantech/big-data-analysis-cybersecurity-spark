import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import arange
import os

# Define the contingency table data
data = {
    'Reliability': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    1: [0, 0, 16, 7, 0, 8, 8, 0, 0, 0],
    2: [804, 149114, 3670, 57653, 4, 2084, 85, 11, 345, 82],
    3: [2225, 3, 6668, 22168, 2, 2151, 156, 7, 260, 79],
    4: [2129, 0, 481, 6447, 0, 404, 43, 2, 58, 24],
    5: [432, 0, 55, 700, 1, 103, 5, 1, 20, 11],
    6: [19, 0, 2, 60, 0, 8, 0, 0, 1, 0],
    7: [3, 0, 0, 5, 0, 0, 0, 0, 2, 0]
}

# Convert the data into a DataFrame
av = pd.DataFrame(data)
av.set_index('Reliability', inplace=True)

# Plot the graphical view of the contingency table
plt.figure(figsize=(10, 8))
plt.pcolor(av, cmap=cm.Greens)
plt.yticks(arange(0.5, len(av.index), 1), av.index)
plt.xticks(arange(0.5, len(av.columns), 1), av.columns)
plt.colorbar()
plt.title('Contingency Table for Risk and Reliability')
plt.xlabel('Risk')
plt.ylabel('Reliability')

# Save the plot to the specified file
file_path = '/app/data/contingency_table_risk_reliability.png'
os.makedirs(os.path.dirname(file_path), exist_ok=True)
plt.savefig(file_path)

print(f"File saved to {file_path}")
