
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
df = pd.read_csv(BASE_DIR / "data" / "processed_commute_data.csv")

OUTPUT_DIR = BASE_DIR / "analysis" / "unit3_charts"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid")

print("=" * 50)
print("UNIT 3 - ADVANCED DATA VISUALIZATION")
print("=" * 50)

# MATPLOTLIB VISUALIZATIONS

# 1. Bar chart
plt.figure(figsize=(9, 5))
mode_counts = df["Transport_Mode"].value_counts()
plt.bar(mode_counts.index, mode_counts.values)
plt.title("Transport Mode Distribution")
plt.xlabel("Transport Mode")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "matplotlib_bar_chart.png", dpi=300)
plt.close()

# 2. Histogram
plt.figure(figsize=(9, 5))
plt.hist(df["Travel_Time_Min"], bins=15, edgecolor="black")
plt.title("Travel Time Distribution")
plt.xlabel("Travel Time (Minutes)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "matplotlib_histogram.png", dpi=300)
plt.close()

# 3. Scatter plot
plt.figure(figsize=(9, 5))
plt.scatter(df["Distance_KM"], df["Travel_Time_Min"])
plt.title("Distance vs Travel Time")
plt.xlabel("Distance (KM)")
plt.ylabel("Travel Time (Minutes)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "matplotlib_scatter.png", dpi=300)
plt.close()

# 4. Pie chart
plt.figure(figsize=(8, 8))
plt.pie(
    mode_counts.values,
    labels=mode_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Transport Mode Share")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "matplotlib_pie_chart.png", dpi=300)
plt.close()

# 5. Box plot
plt.figure(figsize=(9, 5))
plt.boxplot(
    [
        df.loc[df["Transport_Mode"] == mode, "Travel_Time_Min"]
        for mode in mode_counts.index
    ],
    tick_labels=mode_counts.index
)
plt.title("Travel Time by Transport Mode")
plt.xlabel("Transport Mode")
plt.ylabel("Travel Time (Minutes)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "matplotlib_boxplot.png", dpi=300)
plt.close()

# SEABORN VISUALIZATIONS

# 6. Count plot
plt.figure(figsize=(9, 5))
sns.countplot(data=df, x="Transport_Mode", order=mode_counts.index)
plt.title("Student Count by Transport Mode")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "seaborn_countplot.png", dpi=300)
plt.close()

# 7. Box plot
plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x="Transport_Mode", y="Daily_Expense_INR")
plt.title("Daily Expense by Transport Mode")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "seaborn_boxplot.png", dpi=300)
plt.close()

# 8. Violin plot
plt.figure(figsize=(9, 5))
sns.violinplot(data=df, x="Transport_Mode", y="Travel_Time_Min")
plt.title("Travel Time Distribution by Transport Mode")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "seaborn_violinplot.png", dpi=300)
plt.close()

# 9. Scatter plot
plt.figure(figsize=(9, 5))
sns.scatterplot(
    data=df,
    x="Distance_KM",
    y="Travel_Time_Min",
    hue="Transport_Mode"
)
plt.title("Distance and Travel Time by Transport Mode")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "seaborn_scatterplot.png", dpi=300)
plt.close()

# 10. Correlation heatmap
numeric_df = df.select_dtypes(include="number")
plt.figure(figsize=(9, 6))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Between Numerical Variables")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "seaborn_heatmap.png", dpi=300)
plt.close()

# PLOTLY VISUALIZATIONS

# 11. Interactive bar chart
fig = px.bar(
    df["Transport_Mode"].value_counts().reset_index(),
    x="Transport_Mode",
    y="count",
    title="Interactive Transport Mode Distribution"
)
fig.write_html(OUTPUT_DIR / "plotly_bar_chart.html")

# 12. Interactive scatter plot
fig = px.scatter(
    df,
    x="Distance_KM",
    y="Travel_Time_Min",
    color="Transport_Mode",
    hover_data=["Student_ID"],
    title="Interactive Distance vs Travel Time"
)
fig.write_html(OUTPUT_DIR / "plotly_scatter.html")

# 13. Interactive box plot
fig = px.box(
    df,
    x="Transport_Mode",
    y="Daily_Expense_INR",
    color="Transport_Mode",
    title="Interactive Daily Expense Comparison"
)
fig.write_html(OUTPUT_DIR / "plotly_boxplot.html")

# 14. Interactive histogram
fig = px.histogram(
    df,
    x="Travel_Time_Min",
    color="Transport_Mode",
    title="Interactive Travel Time Distribution"
)
fig.write_html(OUTPUT_DIR / "plotly_histogram.html")

# 15. Interactive pie chart
fig = px.pie(
    df,
    names="Transport_Mode",
    title="Interactive Transport Mode Share"
)
fig.write_html(OUTPUT_DIR / "plotly_pie_chart.html")

print("\nUnit 3 completed successfully!")
print("Total visualizations: 15")
print("Matplotlib: 5")
print("Seaborn: 5")
print("Plotly: 5")
print("Charts saved in:", OUTPUT_DIR)
