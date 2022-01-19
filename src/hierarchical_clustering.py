"""
凝集型階層的クラスタリングを行う
"""
import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, fcluster, linkage

from src.input_data import input_data


def hierarchical_clustering(file: str, mode: str, n_clusters: int, title: str):
    """
    データを凝集型階層的クラスタリングによってクラスタリングする

    また、テンドログラムを保存する

    Paramters
    ---------
    file : str
        クラスタリングしたいファイルのパス

        データはカンマ区切り

    mode : str
        クラスタ感の距離の計算方法

    n_clusters : int
        クラスタリングにする個数

    title : str
        データの保存に使用する名前

    Returns
    -------

    data : pandas.DataFrame
        データに加え、クラスタリングのグループ(cluster)を追加したデータ

    data_std : numpy.ndarry
        データを標準化したデータ
    """

    data, data_std = input_data(file)

    # クラスリングの実施
    bind = linkage(data_std,
                   metric='euclidean', method=mode)
    thershold = bind[-n_clusters][2]  # しきい値

    # テンドログラムの保存
    fig = plt.figure(num=None, figsize=(16, 9), dpi=200, facecolor='w',
                     edgecolor='k')
    dendrogram(bind, labels=data.index)
    plt.show()
    fig.savefig(f"output/{title}_dendrogram.png")

    bind_data = pd.DataFrame(
        data=bind, columns=['A', 'B', 'dict(A,B)', '#(A)+#(B)'])
    bind_data = bind_data.astype(
        {'A': int, 'B': int, 'dict(A,B)': float, '#(A)+#(B)': int})
    bind_data.to_csv(f"output/{title}_dendrogram_data.csv", index=True)

    # クラスタリングの実施
    clusters = fcluster(bind, thershold, criterion='distance')
    data["cluster"] = clusters

    return data, data_std
