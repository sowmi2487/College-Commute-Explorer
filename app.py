
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="College Commute Explorer",
    page_icon="🚌",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "college_commute_data.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

# Sidebar
st.sidebar.title("🚌 Commute Explorer")
st.sidebar.caption("Student Transportation Analytics")

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Transport Analysis",
        "Travel Time Analysis",
        "Expense Analysis",
        "Automatic Insights",
        "Data Explorer"
    ]
)

st.sidebar.divider()

modes = ["All"] + sorted(df["Transport_Mode"].dropna().unique().tolist())
selected_mode = st.sidebar.selectbox("Transport Mode", modes)

max_time = st.sidebar.slider(
    "Maximum Travel Time (Minutes)",
    min_value=int(df["Travel_Time_Min"].min()),
    max_value=int(df["Travel_Time_Min"].max()),
    value=int(df["Travel_Time_Min"].max())
)

filtered = df[df["Travel_Time_Min"] <= max_time].copy()

if selected_mode != "All":
    filtered = filtered[filtered["Transport_Mode"] == selected_mode]

# Header
st.title("🚌 College Commute Explorer")
st.caption(
    "Exploratory Data Analysis of Student Transportation Patterns"
)

if filtered.empty:
    st.warning("No records match the selected filters.")
    st.stop()

# Metrics
total = len(filtered)
avg_time = filtered["Travel_Time_Min"].mean()
avg_distance = filtered["Distance_KM"].mean()
avg_expense = filtered["Daily_Expense_INR"].mean()

def show_metrics():
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Students", f"{total}")
    c2.metric("Average Travel Time", f"{avg_time:.1f} min")
    c3.metric("Average Distance", f"{avg_distance:.1f} km")
    c4.metric("Average Daily Expense", f"₹{avg_expense:.1f}")

# Overview
if page == "Overview":
    st.subheader("Dashboard Overview")
    show_metrics()

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        counts = filtered["Transport_Mode"].value_counts().reset_index()
        counts.columns = ["Transport_Mode", "Students"]

        fig = px.pie(
            counts,
            names="Transport_Mode",
            values="Students",
            hole=0.45,
            title="Transport Mode Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.histogram(
            filtered,
            x="Travel_Time_Min",
            color="Transport_Mode",
            title="Travel Time Distribution",
            nbins=15
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Sample Student Records")
    st.dataframe(filtered.head(10), use_container_width=True)

# Transport Analysis
elif page == "Transport Analysis":
    st.subheader("Transport Mode Analysis")
    show_metrics()

    counts = filtered["Transport_Mode"].value_counts().reset_index()
    counts.columns = ["Transport_Mode", "Students"]

    fig = px.bar(
        counts,
        x="Transport_Mode",
        y="Students",
        color="Transport_Mode",
        title="Students Using Each Transport Mode"
    )
    st.plotly_chart(fig, use_container_width=True)

    summary = filtered.groupby("Transport_Mode").agg(
        Student_Count=("Student_ID", "count"),
        Average_Distance=("Distance_KM", "mean"),
        Average_Travel_Time=("Travel_Time_Min", "mean"),
        Average_Expense=("Daily_Expense_INR", "mean")
    ).reset_index()

    st.subheader("Transport Summary")
    st.dataframe(summary.round(2), use_container_width=True)

# Travel Time Analysis
elif page == "Travel Time Analysis":
    st.subheader("Travel Time Analysis")
    show_metrics()

    col1, col2 = st.columns(2)

    with col1:
        fig = px.histogram(
            filtered,
            x="Travel_Time_Min",
            color="Transport_Mode",
            nbins=15,
            title="Travel Time Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.box(
            filtered,
            x="Transport_Mode",
            y="Travel_Time_Min",
            color="Transport_Mode",
            title="Travel Time by Transport Mode"
        )
        st.plotly_chart(fig, use_container_width=True)

    fig = px.scatter(
        filtered,
        x="Distance_KM",
        y="Travel_Time_Min",
        color="Transport_Mode",
        hover_data=["Student_ID"],
        title="Distance vs Travel Time"
    )
    st.plotly_chart(fig, use_container_width=True)

# Expense Analysis
elif page == "Expense Analysis":
    st.subheader("Daily Travel Expense Analysis")
    show_metrics()

    expense = filtered.groupby("Transport_Mode")[
        "Daily_Expense_INR"
    ].mean().reset_index()

    fig = px.bar(
        expense,
        x="Transport_Mode",
        y="Daily_Expense_INR",
        color="Transport_Mode",
        title="Average Daily Expense by Transport Mode",
        labels={"Daily_Expense_INR": "Expense (₹)"}
    )
    st.plotly_chart(fig, use_container_width=True)

    fig = px.box(
        filtered,
        x="Transport_Mode",
        y="Daily_Expense_INR",
        color="Transport_Mode",
        title="Expense Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

# Automatic Insights
elif page == "Automatic Insights":
    st.subheader("🤖 Automatic Data Insights")
    show_metrics()

    popular = filtered["Transport_Mode"].mode()[0]
    fastest = filtered.groupby("Transport_Mode")[
        "Travel_Time_Min"
    ].mean().idxmin()

    cheapest = filtered.groupby("Transport_Mode")[
        "Daily_Expense_INR"
    ].mean().idxmin()

    st.success(f"Most popular transport mode: {popular}")
    st.info(f"Lowest average travel time: {fastest}")
    st.info(f"Lowest average daily expense: {cheapest}")

    insights = [
        f"Total students in the filtered dataset: {total}",
        f"Average travel time: {avg_time:.2f} minutes",
        f"Average travel distance: {avg_distance:.2f} km",
        f"Average daily travel expense: ₹{avg_expense:.2f}",
        f"Most popular transport mode: {popular}",
        f"Lowest average travel time mode: {fastest}",
        f"Lowest average expense mode: {cheapest}"
    ]

    st.subheader("Generated Insights")
    for item in insights:
        st.write("•", item)

    report = "\n".join(insights)
    st.download_button(
        "Download Insights Report",
        report,
        file_name="commute_insights.txt",
        mime="text/plain"
    )

# Data Explorer
elif page == "Data Explorer":
    st.subheader("📊 Explore Student Records")
    show_metrics()

    st.dataframe(filtered, use_container_width=True)

    csv = filtered.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Filtered Dataset",
        csv,
        file_name="filtered_commute_data.csv",
        mime="text/csv"
    )

st.divider()
st.caption(
    "College Commute Explorer | EDA Units 1–3 | "
    "Dataset contains simulated student records."
)
