import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.feature_selection import RFE

df = pd.read_csv("zomato.csv")

X = df.drop(
    "average_cost_for_two",
    axis=1
)

y = df["average_cost_for_two"]

model = DecisionTreeRegressor()

rfe = RFE(
    estimator=model,
    n_features_to_select=3
)

rfe.fit(X, y)

selected_features = X.columns[rfe.support_]

print("Selected Features:")
print(selected_features)

print("\nFeature Rankings:")

for feature, rank in zip(
    X.columns,
    rfe.ranking_
):
    print(feature, ":", rank)