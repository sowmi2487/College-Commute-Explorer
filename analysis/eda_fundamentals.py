
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Load dataset
BASE_DIR = Path(__file__).resolve().parent.parent
df = pd.read_csv(BASE_DIR / "data" / "college_commute_data.csv")

print("=" * 50)
print("UNIT 1 - EDA FUNDAMENTALS")
print("=" * 50)

# 1. Dataset overview
print("\n1. DATASET INFORMATION")
print(df.info())

print("\n2. FIRST FIVE RECORDS")
print(df.head())

# 2. Descriptive statistics
print("\n3. DESCRIPTIVE STATISTICS")
print(df.describe(include="all"))

# 3. Data types
print("\n4. DATA TYPES")
print(df.dtypes)

# 4. Missing values
print("\n5. MISSING VALUES")
print(df.isnull().sum())

# 5. Duplicate records
print("\n6. DUPLICATE RECORDS")
print(df.duplicated().sum())

# 6. Categorical frequency
print("\n7. TRANSPORT MODE FREQUENCY")
print(df["Transport_Mode"].value_counts())

# Create output folder
output_dir = BASE_DIR / "analysis" / "unit1_charts"
output_dir.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid")

# Chart 1: Transport mode distribution
plt.figure(figsize=(9, 5))
sns.countplot(data=df, x="Transport_Mode", order=df["Transport_Mode"].value_counts().index)
plt.title("Student Transport Mode Distribution")
plt.xlabel("Transport Mode")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(output_dir / "transport_distribution.png", dpi=300)
plt.close()

# Chart 2: Travel time distribution
plt.figure(figsize=(9, 5))
sns.histplot(df["Travel_Time_Min"], bins=15, kde=True)
plt.title("Distribution of Student Travel Time")
plt.xlabel("Travel Time (Minutes)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(output_dir / "travel_time_distribution.png", dpi=300)
plt.close()

# Chart 3: Daily travel expense
plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x="Transport_Mode", y="Daily_Expense_INR")
plt.title("Daily Travel Expense by Transport Mode")
plt.xlabel("Transport Mode")
plt.ylabel("Daily Expense (INR)")
plt.tight_layout()
plt.savefig(output_dir / "expense_boxplot.png", dpi=300)
plt.close()

# Chart 4: Distance vs travel time
plt.figure(figsize=(9, 5))
sns.scatterplot(data=df, x="Distance_KM", y="Travel_Time_Min", hue="Transport_Mode")
plt.title("Distance vs Travel Time")
plt.xlabel("Distance (KM)")
plt.ylabel("Travel Time (Minutes)")
plt.tight_layout()
plt.savefig(output_dir / "distance_vs_time.png", dpi=300)
plt.close()

print("\nUnit 1 analysis completed successfully!")
print("Charts saved in:", output_dir)
