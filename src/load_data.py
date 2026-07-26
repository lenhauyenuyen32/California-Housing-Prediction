from sklearn.datasets import fetch_california_housing


def load_dataset():
    housing = fetch_california_housing(as_frame=True)
    return housing.frame