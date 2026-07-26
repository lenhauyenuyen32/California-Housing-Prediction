from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing(as_frame=True)

print(housing.frame.head())