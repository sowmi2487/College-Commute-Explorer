# Chennai Air Quality Detective 🌍

## Chennai Air Pollution Pattern Analysis Using Bivariate, Multivariate and Time Series EDA

### 1. Project Overview

Chennai Air Quality Detective is an Exploratory Data Analysis project that analyzes simulated air pollution data across three regions of Chennai: North Chennai, Central Chennai and South Chennai.

The project applies Bivariate Analysis, Multivariate Analysis and Time Series Analysis to identify relationships between pollutants, compare pollution patterns across locations and study changes over time.

### 2. Project Objectives

- Generate and analyze hourly air-quality data.
- Identify relationships between different air pollutants.
- Perform station-wise pollution comparisons.
- Analyze hourly, daily and monthly pollution trends.
- Apply statistical operations and data visualization.
- Develop an interactive dashboard using Streamlit.

### 3. Technologies and Libraries Used

| Library | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation, cleaning and analysis |
| NumPy | Numerical calculations and synthetic data generation |
| Matplotlib | Statistical charts and time-series plots |
| Seaborn | Correlation heatmaps, boxplots and pairplots |
| Plotly | Interactive visualizations |
| Streamlit | Interactive web dashboard |
| Pathlib | File and directory management |

### 4. Project Folder Structure

```text
Chennai-Air-Quality-Detective/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── generate_air_quality_data.py
│   └── chennai_air_quality.csv
│
└── analysis/
    ├── bivariate_multivariate.py
    ├── time_series_analysis.py
    │
    ├── unit4_charts/
    │   ├── correlation_heatmap.png
    │   ├── multivariate_pairplot.png
    │   ├── pm25_vs_pm10.png
    │   └── other charts
    │
    └── unit5_charts/
        ├── hourly_pm25_trend.png
        ├── daily_pm25_trend.png
        ├── monthly_pm25_trend.png
        ├── rolling_average.png
        ├── monthly_seasonality.png
        └── pollution_index_timeseries.png
```

### 5. Important Python Files and Their Uses

**A. generate_air_quality_data.py**

Purpose:
- Generates the synthetic air-quality dataset.
- Creates hourly timestamps for the year 2025.
- Simulates pollutant concentrations for three Chennai stations.
- Introduces missing values for practicing data cleaning.
- Saves the generated records as a CSV file.

Important code:

```python
dates = pd.date_range(
    start="2025-01-01",
    end="2025-12-31 23:00:00",
    freq="h"
)
```

Use: Generates hourly timestamps throughout 2025.

```python
df.to_csv(output_path, index=False)
```

Use: Exports the generated dataset into CSV format.

**B. bivariate_multivariate.py**

Purpose:
- Performs Bivariate and Multivariate EDA.
- Studies relationships between PM2.5, PM10, NO2, SO2, CO and O3.
- Compares pollutant levels across Chennai stations.
- Generates nine visualizations.

Important code:

```python
sns.scatterplot(
    data=df,
    x="PM2_5",
    y="PM10",
    hue="Station"
)
```

Use: Examines the relationship between PM2.5 and PM10 across different stations.

```python
correlation = df[numeric_cols].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)
```

Use: Calculates and visualizes correlations between numerical pollutant variables.

```python
sns.pairplot(
    pair_data,
    vars=["PM2_5", "PM10", "NO2", "SO2", "CO", "O3"],
    hue="Station",
    corner=True
)
```

Use: Displays pairwise relationships between multiple pollutants.

**C. time_series_analysis.py**

Purpose:
- Performs time-based pollution analysis.
- Studies hourly, daily and monthly PM2.5 trends.
- Calculates rolling averages.
- Examines monthly seasonality.
- Generates six time-series visualizations.

Important code:

```python
hourly = (
    df.groupby(df["Timestamp"].dt.hour)["PM2_5"]
    .mean()
)
```

Use: Calculates the average PM2.5 concentration for each hour of the day.

```python
df["PM2_5_Rolling"] = (
    df.groupby("Station")["PM2_5"]
    .transform(
        lambda x: x.rolling(
            window=24,
            min_periods=1
        ).mean()
    )
)
```

Use: Calculates a 24-hour rolling average separately for each station to smooth short-term fluctuations.

```python
monthly_data["Month"] = (
    monthly_data["Timestamp"].dt.month
)

monthly = (
    monthly_data.groupby(["Month", "Station"])["PM2_5"]
    .mean()
    .reset_index()
)
```

Use: Calculates monthly average PM2.5 values for each station.

**D. app.py**

Purpose:
- Creates an interactive air-quality dashboard using Streamlit.
- Displays pollution statistics and visualizations.
- Provides station, pollutant and date filters.
- Supports pollutant relationship analysis and station comparisons.
- Displays time-series trends.
- Generates automatic insights.
- Allows users to download filtered datasets and insight reports.

Important code:

```python
@st.cache_data
def load_data():
    data = pd.read_csv(DATA_PATH)
    data["Timestamp"] = pd.to_datetime(data["Timestamp"])
    return data
```

Use: Loads and caches the dataset to improve dashboard performance.

```python
fig = px.scatter(
    filtered,
    x=x_variable,
    y=y_variable,
    color="Station"
)

st.plotly_chart(fig, use_container_width=True)
```

Use: Displays interactive pollutant relationship visualizations.

```python
st.download_button(
    "Download Filtered Dataset",
    csv,
    file_name="chennai_air_quality_filtered.csv",
    mime="text/csv"
)
```

Use: Allows users to download the filtered dataset as a CSV file.

### 6. Exploratory Data Analysis Units

#### Unit 4 – Bivariate and Multivariate Analysis

Bivariate Analysis:
- PM2.5 vs PM10
- NO2 vs CO
- O3 vs PM2.5
- Station-wise PM2.5 comparison

Multivariate Analysis:
- Correlation heatmap
- Pair plot
- Station-wise pollutant comparison
- Multivariate bubble plot
- Pollution index distribution

Total visualizations: 9.

#### Unit 5 – Time Series Analysis

- Hourly PM2.5 trend
- Daily PM2.5 trend
- Monthly PM2.5 trend
- 24-hour rolling average
- Monthly seasonality analysis
- Pollution index time series

Total visualizations: 6.

### 7. Dataset Description

The dataset contains 26,280 hourly records covering three simulated Chennai stations during 2025.

| Column | Description |
|---|---|
| Timestamp | Date and time of observation |
| Station | Simulated Chennai monitoring station |
| PM2_5 | Fine particulate matter concentration |
| PM10 | Particulate matter concentration |
| NO2 | Nitrogen dioxide |
| SO2 | Sulphur dioxide |
| CO | Carbon monoxide |
| O3 | Ozone |
| Simulated_Pollution_Index | Academically constructed pollution indicator |

**Dataset Disclaimer:** The dataset is synthetically generated for academic purposes. The Simulated_Pollution_Index is not the official CPCB Air Quality Index (AQI), and the records do not represent actual Chennai pollution measurements.

### 8. How to Run the Project

Install the required libraries:

```bash
pip install -r requirements.txt
```

Generate the dataset:

```bash
python data/generate_air_quality_data.py
```

Run Unit 4:

```bash
python analysis/bivariate_multivariate.py
```

Run Unit 5:

```bash
python analysis/time_series_analysis.py
```

Launch the interactive dashboard:

```bash
streamlit run app.py
```

### 9. Expected Outcome

The project provides an interactive analytical platform for exploring simulated air pollution patterns across Chennai stations. It demonstrates how Python-based exploratory data analysis, statistical techniques, time-series methods and interactive visualizations can be combined to understand environmental datasets.

### 10. Project Information

**Project Name:** Chennai Air Quality Detective

**Project Category:** Exploratory Data Analysis

**Units Covered:** Unit 4 and Unit 5

**Implementation:** Python-based EDA and Streamlit Dashboard
