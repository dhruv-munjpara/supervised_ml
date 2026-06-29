import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("ipl_players.csv")

# Select numeric columns
numeric_cols = ["runs", "wickets", "matches", "strike_rate"]

# Apply StandardScaler
scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Save scaled dataset
df.to_csv("ipl_scaled.csv", index=False)

print(df.head())
print("\nScaled data saved as ipl_scaled.csv")