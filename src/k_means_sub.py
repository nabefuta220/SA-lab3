"""
k_meansによる処理を行う
"""

from sklearn.cluster import KMeans

from src.input_data import input_data


def k_means(file: str, n_clusters: int):
    """
    データをk-meansによってクラスタリングする

    Paramters
    ---------
    file : str
        クラスタリングしたいファイルのパス

        データはカンマ区切り

    n_clusters : int
        クラスタリングにする個数


    Returns
    -------

    data : pandas.DataFrame
        データに加え、クラスタリングのグループ(cluster)を追加したデータ

    data_std : numpy.ndarry
        データを標準化したデータ
    """

    data, data_std = input_data(
        file)
    k_meaner = KMeans(n_clusters, random_state=0)
    clusters = k_meaner.fit_predict(data_std)
    data["cluster"] = clusters

    return data, data_std
