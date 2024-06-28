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

# Setup new crosstab structures
typ = data['newtype']
rel = data['Reliability']
rsk = data['Risk']

# Compute crosstab making it split on the new type column
xtab = pd.crosstab(typ, [rel, rsk], rownames=['typ'], colnames=['rel', 'rsk'])

# Print the contingency table for reference
print(xtab.to_string())  # Output not shown

# Plot the contingency table
xtab.plot(kind='bar', legend=False, title="Risk | Reliability | Type").grid(False)

# Save the plot to a specified file
output_file_path = '/app/data/risk_reliability_type_bar_chart.png'
plt.savefig(output_file_path)

print(f"File saved to {output_file_path}")

########################################################
## LOGARITHMIC SCALING ADDED BELOW
########################################################

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

# Setup new crosstab structures
typ = data['newtype']
rel = data['Reliability']
rsk = data['Risk']

# Compute crosstab making it split on the new type column
xtab = pd.crosstab(typ, [rel, rsk], rownames=['typ'], colnames=['rel', 'rsk'])

# Print the contingency table for reference
print(xtab.to_string())  # Output not shown

# Plot the contingency table
plt.figure(figsize=(14, 8))  # Adjust the figure size for better readability
xtab.plot(kind='bar', legend=False, title="Risk | Reliability | Type", logy=True).grid(False)  # Use log scale for Y axis

# Adjust X axis labels for better visibility
plt.xticks(rotation=45, ha='right')
plt.xlabel('Type | (Reliability, Risk)')
plt.ylabel('Count (log scale)')

# Save the plot to a specified file
output_file_path = '/app/data/risk_reliability_type_bar_chart_logarithmic_scaling.png'
plt.savefig(output_file_path, bbox_inches='tight')  # Ensure labels are not cut off

print(f"File saved to {output_file_path}")


