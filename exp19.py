import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("covid_data.csv")

# Inspect
print(df.head())
print(df.info())
print(df.describe())

# Cleaning
df = df.drop_duplicates()
df = df.fillna(0)

# Aggregation
total_cases = df.groupby("Country")["Cases"].sum()
print(total_cases)

# Plot
df["Cases"].plot()
plt.title("COVID Cases Trend")
plt.show()

# Histogram
df["Cases"].hist()
plt.show()

# Scatter
plt.scatter(df["Cases"], df["Deaths"])
plt.show()