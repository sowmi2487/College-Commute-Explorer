
import pandas as pd
import numpy as np
from pathlib import Path

# Reproducible synthetic dataset
np.random.seed(42)

n = 150

# Transport mode distribution
transport_modes = (
    ["Bus"] * 69
    + ["Bike"] * 36
    + ["Train"] * 21
    + ["Car"] * 12
    + ["Walk"] * 12
)

np.random.shuffle(transport_modes)

data = []

for i in range(n):
    mode = transport_modes[i]

    # Generate values based on transport mode
    if mode == "Bus":
        distance = np.random.uniform(3, 25)
        travel_time = np.random.randint(20, 75)
        expense = np.random.randint(10, 50)

    elif mode == "Bike":
        distance = np.random.uniform(2, 20)
        travel_time = np.random.randint(10, 45)
        expense = np.random.randint(15, 60)

    elif mode == "Train":
        distance = np.random.uniform(5, 35)
        travel_time = np.random.randint(25, 80)
        expense = np.random.randint(10, 40)

    elif mode == "Car":
        distance = np.random.uniform(3, 30)
        travel_time = np.random.randint(15, 60)
        expense = np.random.randint(50, 200)

    else:  # Walk
        distance = np.random.uniform(0.5, 3)
        travel_time = np.random.randint(10, 40)
        expense = 0

    departure_hour = np.random.randint(7, 10)
    departure_minute = np.random.choice([0, 10, 15, 20, 30, 45])

    arrival_total = departure_hour * 60 + departure_minute + travel_time
    arrival_hour = (arrival_total // 60) % 24
    arrival_minute = arrival_total % 60

    convenience = np.random.choice(
        ["Low", "Medium", "High"],
        p=[0.2, 0.4, 0.4]
    )

    transfers = (
        np.random.randint(1, 4)
        if mode in ["Bus", "Train"]
        else 0
    )

    data.append({
        "Student_ID": f"STU{i + 1:03d}",
        "Transport_Mode": mode,
        "Distance_KM": round(distance, 2),
        "Travel_Time_Min": travel_time,
        "Daily_Expense_INR": expense,
        "Departure_Time": f"{departure_hour:02d}:{departure_minute:02d}",
        "Arrival_Time": f"{arrival_hour:02d}:{arrival_minute:02d}",
        "Transfers": transfers,
        "Travel_Convenience": convenience
    })

df = pd.DataFrame(data)

# Introduce missing values for EDA practice
for column in ["Distance_KM", "Daily_Expense_INR", "Travel_Convenience"]:
    missing_indices = np.random.choice(df.index, 4, replace=False)
    df.loc[missing_indices, column] = np.nan

# Save dataset
output_path = Path(__file__).parent / "college_commute_data.csv"
df.to_csv(output_path, index=False)

print("Dataset generated successfully!")
print("Total records:", len(df))
print("\nTransport mode distribution:")
print(df["Transport_Mode"].value_counts())
print("\nMissing values:")
print(df.isnull().sum())
print("\nDataset saved to:", output_path)
