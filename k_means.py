"""
k-meansを使ってクラスタリングを行う
"""
from src.k_means_sub import k_means
from src.analyze import analyze_data
from src.visilze import plot_data
if __name__ == "__main__":

    data, data_std = k_means("output/customerData.txt", 4)

    print(data.head())

    analyze_data(data, "k-means")

    plot_data(data, data_std, "k-means")
