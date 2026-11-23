
import pandas as pd
import numpy as np
from pathlib import Path

# Load dataset
BASE_DIR = Path(__file__).resolve().parent.parent
df = pd.read_csv(BASE_DIR / "data" / "college_commute_data.csv")

print("=" * 55)
print("UNIT 2 - ADVANCED PANDAS OPERATIONS")
print("=" * 55)

# 1. Series
print("\n1. SERIES")
mode_series = df["Transport_Mode"]
print(mode_series.head())
print("Series type:", type(mode_series))

# 2. DataFrame
print("\n2. DATAFRAME")
print(df.head())
print("DataFrame shape:", df.shape)

# 3. Indexing and selection
print("\n3. INDEXING AND SELECTION")
print(df.loc[0:4, ["Student_ID", "Transport_Mode", "Travel_Time_Min"]])
print(df.iloc[0:5, 0:4])

# 4. Conditional filtering
print("\n4. CONDITIONAL FILTERING")
long_commute = df[df["Travel_Time_Min"] > 40]
print(long_commute.head())
print("Students with travel time above 40 minutes:", len(long_commute))

# 5. Missing value handling
print("\n5. MISSING VALUE HANDLING")
print("Missing values before:")
print(df.isnull().sum())

clean_df = df.copy()
clean_df["Distance_KM"] = clean_df["Distance_KM"].fillna(
    clean_df["Distance_KM"].median()
)
clean_df["Daily_Expense_INR"] = clean_df["Daily_Expense_INR"].fillna(
    clean_df["Daily_Expense_INR"].median()
)
clean_df["Travel_Convenience"] = clean_df["Travel_Convenience"].fillna(
    clean_df["Travel_Convenience"].mode()[0]
)

print("Missing values after:")
print(clean_df.isnull().sum())

# 6. MultiIndex
print("\n6. MULTIINDEX")
multi_df = clean_df.set_index(["Transport_Mode", "Student_ID"])
print(multi_df.head(10))

# 7. Concatenation
print("\n7. CONCATENATION")
part1 = clean_df.iloc[:75]
part2 = clean_df.iloc[75:]
concat_df = pd.concat([part1, part2], ignore_index=True)
print("Concatenated shape:", concat_df.shape)

# 8. Append replacement using concat
print("\n8. APPEND REPLACEMENT")
sample_new = pd.DataFrame([{
    "Student_ID": "STU151",
    "Transport_Mode": "Bus",
    "Distance_KM": 12.5,
    "Travel_Time_Min": 35,
    "Daily_Expense_INR": 25,
    "Departure_Time": "08:00",
    "Arrival_Time": "08:35",
    "Transfers": 1,
    "Travel_Convenience": "High"
}])

appended_df = pd.concat([clean_df, sample_new], ignore_index=True)
print("Shape after appending:", appended_df.shape)

# 9. Merge
print("\n9. MERGE")
profile_df = clean_df[["Student_ID", "Transport_Mode", "Distance_KM"]]
expense_df = clean_df[["Student_ID", "Daily_Expense_INR"]]

merged_df = pd.merge(
    profile_df,
    expense_df,
    on="Student_ID",
    how="inner"
)
print(merged_df.head())

# 10. Join
print("\n10. JOIN")
profile_indexed = profile_df.set_index("Student_ID")
expense_indexed = expense_df.set_index("Student_ID")

joined_df = profile_indexed.join(expense_indexed, how="inner")
print(joined_df.head())

# 11. GroupBy
print("\n11. GROUPBY")
grouped_df = clean_df.groupby("Transport_Mode").agg(
    Average_Distance=("Distance_KM", "mean"),
    Average_Travel_Time=("Travel_Time_Min", "mean"),
    Average_Expense=("Daily_Expense_INR", "mean"),
    Student_Count=("Student_ID", "count")
)
print(grouped_df.round(2))

# 12. Pivot table
print("\n12. PIVOT TABLE")
pivot_df = pd.pivot_table(
    clean_df,
    index="Transport_Mode",
    values=["Distance_KM", "Travel_Time_Min", "Daily_Expense_INR"],
    aggfunc="mean"
)
print(pivot_df.round(2))

# 13. Vectorized string operations
print("\n13. VECTORIZED STRING OPERATIONS")
string_df = clean_df.copy()

string_df["Transport_Mode"] = (
    string_df["Transport_Mode"].str.upper()
)
string_df["Student_ID"] = (
    string_df["Student_ID"].str.replace("STU", "STUDENT-", regex=False)
)

print(string_df[["Student_ID", "Transport_Mode"]].head())

# 14. Sorting
print("\n14. SORTING")
sorted_df = clean_df.sort_values(
    by="Travel_Time_Min",
    ascending=False
)
print(sorted_df[["Student_ID", "Transport_Mode", "Travel_Time_Min"]].head(10))

# 15. Export processed data
output_path = BASE_DIR / "data" / "processed_commute_data.csv"
clean_df.to_csv(output_path, index=False)

print("\nUnit 2 completed successfully!")
print("Processed dataset saved at:", output_path)
