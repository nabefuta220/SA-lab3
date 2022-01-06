"""
k-meansを使ってクラスタリングを行う
"""
from src.k_means_sub import k_means

if __name__ == "__main__":

    data, data_std = k_means("output/customerData.txt", 4)

    print(data.head())
    print(data["cluster"].value_counts())
