import matplotlib.pyplot as plt
import seaborn as sns


def show_basic_info(df):
    print(df.head())
    print(df.info())
    print(df.describe())


def plot_histogram(df):
    df.hist(figsize=(12, 8))
    plt.tight_layout()
    plt.savefig("outputs/histogram.png")
    plt.show()


def correlation(df):
    plt.figure(figsize=(10, 8))

    sns.heatmap(
        df.corr(),
        annot=True,
        cmap="coolwarm"
    )

    plt.tight_layout()

    plt.savefig("outputs/correlation.png")

    plt.show()