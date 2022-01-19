"""
単連結法を使ってクラスタリングを行う
"""
from src.analyze import analyze_data
from src.hierarchical_clustering import hierarchical_clustering
from src.visilze import plot_data

if __name__ == "__main__":

    data, data_std = hierarchical_clustering(
        "output/customerData.txt", 'single',4,'single')

    print(data.head())

    analyze_data(data, "single")

    plot_data(data, data_std, "single")
