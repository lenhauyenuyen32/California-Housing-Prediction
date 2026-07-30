import matplotlib.pyplot as plt

def plot_result(df):
    # ===== RMSE =====
    plt.figure(figsize=(10,5))
    plt.bar(df["Model"], df["RMSE"])
    plt.title("Model Comparison - RMSE")
    plt.ylabel("RMSE")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig("outputs/model_comparison_rmse.png")
    plt.close()

    # ===== MAE =====
    plt.figure(figsize=(10,5))
    plt.bar(df["Model"], df["MAE"])
    plt.title("Model Comparison - MAE")
    plt.ylabel("MAE")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig("outputs/model_comparison_mae.png")
    plt.close()

    # ===== R2 =====
    plt.figure(figsize=(10,5))
    plt.bar(df["Model"], df["R2"])
    plt.title("Model Comparison - R² Score")
    plt.ylabel("R² Score")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig("outputs/model_comparison_r2.png")
    plt.close()

    # Hiển thị biểu đồ cuối cùng
    plt.figure(figsize=(10,5))
    plt.bar(df["Model"], df["RMSE"])
    plt.title("Model Comparison - RMSE")
    plt.ylabel("RMSE")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.show()