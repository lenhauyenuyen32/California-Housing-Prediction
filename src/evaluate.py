import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

def evaluate_all(models, X_train, X_test, y_train, y_test):

    results = []

    for name, model in models.items():

        model.fit(X_train, y_train)

        pred = model.predict(X_test)

        mae = mean_absolute_error(y_test, pred)

        rmse = mean_squared_error(
            y_test,
            pred
        ) ** 0.5

        r2 = r2_score(y_test, pred)

        results.append([
            name,
            mae,
            rmse,
            r2
        ])

    df = pd.DataFrame(
        results,
        columns=[
            "Model",
            "MAE",
            "RMSE",
            "R2"
        ]
    )

    df = df.sort_values(
        by="RMSE",
        ascending=True
    )

    print(df)

    return df