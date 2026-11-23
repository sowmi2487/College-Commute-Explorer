# College Commute Explorer 🚌

## Student Commute Pattern Analysis Using Exploratory Data Analysis

### 1. Project Overview

College Commute Explorer is an Exploratory Data Analysis project developed to understand student transportation patterns, travel time, commuting distance and daily travel expenses.

The project uses Python libraries to perform data cleaning, statistical analysis, advanced Pandas operations and data visualization. An interactive dashboard is developed using Streamlit to explore commuting patterns and generate automatic insights.

### 2. Project Objectives

- Analyze student transportation preferences.
- Identify the most commonly used transport modes.
- Study the relationship between commuting distance and travel time.
- Analyze daily transportation expenses.
- Perform data cleaning and missing-value handling.
- Apply advanced Pandas operations.
- Create statistical and interactive visualizations.
- Develop an interactive dashboard for exploring student commute data.

### 3. Technologies and Libraries Used

| Library | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations and dataset generation |
| Matplotlib | Statistical data visualization |
| Seaborn | Statistical charts and graphical analysis |
| Plotly | Interactive charts and visualizations |
| Streamlit | Interactive dashboard development |
| Pathlib | File and directory management |

### 4. Project Folder Structure

```text
College-Commute-Explorer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── generate_dataset.py
│   ├── college_commute_data.csv
│   └── processed_commute_data.csv
│
└── analysis/
    ├── eda_fundamentals.py
    ├── pandas_operations.py
    ├── advanced_visualization.py
    │
    └── unit3_charts/
        ├── matplotlib_bar_chart.png
        ├── matplotlib_histogram.png
        ├── matplotlib_scatter.png
        ├── matplotlib_pie_chart.png
        ├── matplotlib_boxplot.png
        ├── seaborn_countplot.png
        ├── seaborn_boxplot.png
        ├── seaborn_violinplot.png
        ├── seaborn_scatterplot.png
        ├── seaborn_heatmap.png
        └── Plotly interactive HTML charts
```

### 5. Important Python Files and Their Uses

**A. generate_dataset.py**

Purpose:
- Generates a synthetic student commuting dataset.
- Creates 150 student records.
- Includes different transportation modes.
- Generates distance, travel time and daily expense values.
- Introduces missing values for data-cleaning practice.
- Exports the dataset into CSV format.

Important code:

```python
np.random.seed(42)

n = 150

df = pd.DataFrame(data)
```

Use: Generates reproducible synthetic student commute records.

```python
df.to_csv(output_path, index=False)
```

Use: Saves the generated dataset as a CSV file.

**B. eda_fundamentals.py – Unit 1**

Purpose:
- Performs initial dataset exploration.
- Examines dataset structure and data types.
- Calculates descriptive statistics.
- Identifies missing and duplicate values.
- Studies transportation frequency.
- Generates basic statistical visualizations.

Important code:

```python
df.info()
```

Use: Displays dataset information, including columns, data types and non-null counts.

```python
df.describe(include="all")
```

Use: Generates descriptive statistical summaries.

```python
df.isnull().sum()
```

Use: Identifies the number of missing values in each column.

```python
sns.countplot(
    data=df,
    x="Transport_Mode"
)
```

Use: Visualizes the number of students using each transportation mode.

**C. pandas_operations.py – Unit 2**

Purpose:
- Demonstrates advanced Pandas operations.
- Performs Series and DataFrame operations.
- Uses indexing and conditional filtering.
- Handles missing values.
- Implements MultiIndex.
- Performs concatenation, merging and joining.
- Uses GroupBy and pivot tables.
- Demonstrates vectorized string operations.

Important code:

```python
clean_df["Distance_KM"] = (
    clean_df["Distance_KM"].fillna(
        clean_df["Distance_KM"].median()
    )
)
```

Use: Replaces missing distance values with the median.

```python
merged_df = pd.merge(
    profile_df,
    expense_df,
    on="Student_ID",
    how="inner"
)
```

Use: Combines student profile and expense information using Student_ID.

```python
grouped_df = clean_df.groupby(
    "Transport_Mode"
).agg(
    Average_Travel_Time=("Travel_Time_Min", "mean"),
    Average_Expense=("Daily_Expense_INR", "mean")
)
```

Use: Calculates
