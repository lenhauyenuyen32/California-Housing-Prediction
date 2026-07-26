from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

from src.models import models
from src.evaluate import evaluate_all
from src.visualization import plot_result

housing = fetch_california_housing(as_frame=True)

df = housing.frame

X = df.drop("MedHouseVal", axis=1)

y = df["MedHouseVal"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

result = evaluate_all(
    models,
    X_train,
    X_test,
    y_train,
    y_test
)

plot_result(result)