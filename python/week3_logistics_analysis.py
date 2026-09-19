# Full analysis was used to generate the report and visualizations.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the supplied hypothetical dataset
df = pd.read_csv('week3_logistics_dataset.csv')

print(df.describe())
print(df.corr(numeric_only=True))

plt.hist(df['Delivery_Time_min'], bins=20)
plt.title('Distribution of Delivery Time')
plt.xlabel('Delivery Time (minutes)')
plt.ylabel('Number of Shipments')
plt.show()

plt.scatter(df['Distance_km'], df['Delivery_Time_min'], alpha=0.65)
plt.title('Distance vs Delivery Time')
plt.xlabel('Distance (km)')
plt.ylabel('Delivery Time (minutes)')
plt.show()
