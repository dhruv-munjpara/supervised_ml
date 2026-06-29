import pandas as pd

df = pd.read_csv("bookmyshow.csv")

Q1 = df["user_rating"].quantile(0.25)

Q3 = df["user_rating"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

original_rows = len(df)

clean_df = df[
    (df["user_rating"] >= lower_bound)
    &
    (df["user_rating"] <= upper_bound)
]

removed_rows = original_rows - len(clean_df)

print("Rows Removed:", removed_rows)

print("\nClean Dataset")
print(clean_df)