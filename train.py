import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_california_housing

# ==========================
# 1. Đọc dữ liệu
# ==========================
housing = fetch_california_housing(as_frame=True)
df = housing.frame

print("=" * 60)
print("Kích thước dữ liệu:")
print(df.shape)

print("=" * 60)
print("Tên các cột:")
print(df.columns)

print("=" * 60)
print("Kiểu dữ liệu:")
print(df.dtypes)

print("=" * 60)
print("Số lượng giá trị bị thiếu:")
print(df.isnull().sum())

print("=" * 60)
print("Thống kê:")
print(df.describe())

# ==========================
# 2. Histogram
# ==========================
df.hist(figsize=(12,8))

plt.tight_layout()

plt.savefig("histogram.png")

plt.show()