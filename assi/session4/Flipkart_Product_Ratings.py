import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("flipkart_products.csv")

print("Before Scaling")

for col in df.columns:
    print(f"{col}: Min={df[col].min()}, Max={df[col].max()}")

scaler = MinMaxScaler()

scaled_data = scaler.fit_transform(df)

scaled_df = pd.DataFrame(
    scaled_data,
    columns=df.columns
)

print("\nAfter Scaling")

for col in scaled_df.columns:
    print(
        f"{col}: Min={scaled_df[col].min()}, Max={scaled_df[col].max()}"
    )