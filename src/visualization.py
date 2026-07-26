import matplotlib.pyplot as plt

def plot_result(df):

    plt.figure(figsize=(10,5))

    plt.bar(
        df["Model"],
        df["RMSE"]
    )

    plt.xticks(rotation=20)

    plt.ylabel("RMSE")

    plt.tight_layout()

    plt.savefig("outputs/model_comparison.png")

    plt.show()