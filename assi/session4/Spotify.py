import pandas as pd

df = pd.read_csv("spotify_songs.csv")

corr_matrix = df.corr()

print(corr_matrix["popularity"])

correlation = corr_matrix["popularity"].abs()

selected = (
    correlation
    .sort_values(ascending=False)
    .drop("popularity")
    .head(2)
)

print("\nTop 2 Features:")
print(selected) 