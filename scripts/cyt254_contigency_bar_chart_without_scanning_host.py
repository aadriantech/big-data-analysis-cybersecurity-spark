import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the path to the data file
file_path = '/app/data/reputation.data'

# Read the data from the file
column_names = ['IP', 'Risk', 'Reliability', 'Type', 'Country', 'City', 'Coordinates', 'Other']
data = pd.read_csv(file_path, sep='#', names=column_names)

# Create new column as a copy of Type column
data['newtype'] = data['Type']

# Replace multi-Type entries with "Multiples"
data.loc[data['newtype'].str.contains(";"), 'newtype'] = "Multiples"

# Filter out all "Scanning Hosts"
rrt_df = data[data['newtype'] != "Scanning Host"]

# Setup new crosstab structures
typ = rrt_df['newtype']
rel = rrt_df['Reliability']
rsk = rrt_df['Risk']

# Compute crosstab making it split on the new type column
xtab = pd.crosstab(typ, [rel, rsk], rownames=['typ'], colnames=['rel', 'rsk'])

# Plot the contingency table
plt.figure(figsize=(14, 8))
xtab.plot(kind='bar', legend=False, title="Risk | Reliability | Type (Without Scanning Host)").grid(False)

# Adjust X axis labels for better visibility
plt.xticks(rotation=45, ha='right')
plt.xlabel('Type | (Reliability, Risk)')
plt.ylabel('Count')

# Save the plot to a specified file
output_file_path = '/app/data/risk_reliability_type_without_scanning_host_bar_chart.png'
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
plt.savefig(output_file_path, bbox_inches='tight')

print(f"File saved to {output_file_path}")
