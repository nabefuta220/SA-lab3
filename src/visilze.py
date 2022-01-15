"""
データを2次元に落とし込み、表示する
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA


def plot_data(data:pd.DataFrame, data_std:np.ndarray, title: str):
    """
    データを2次元に落とし込み、プロットする

    Paramters
    --------
    data : pandas.DataFrame
        データに加え、クラスタリングのグループ(cluster)を追加したデータ

    data_std : numpy.ndarray
        データを標準化したデータ
    title : str
        データの保存に使用する名前
    """
    pcaer = PCA(n_components=2)
    pcaer.fit(data_std)
    x_pca = pcaer.transform(data_std)
    pca_df = pd.DataFrame(x_pca)
    pca_df["cluster"] = data["cluster"]
    print(f"explained_varience_radio_ :{pcaer.explained_variance_ratio_}")
    print(f"compopnents :\n{pcaer.components_}")
    print(f"mean :\n{pcaer.mean_}")
    print(f"covariance :\n{pcaer.get_covariance()}")
    fig = plt.figure(figsize=(6, 6))
    for i in data["cluster"].unique():
        tmp = pca_df.loc[pca_df["cluster"] == i]
        plt.scatter(tmp[0], tmp[1], label=f"cluster{i}", alpha=.7)
        plt.legend()
        plt.grid()
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title(f"{title}_distribute")
    plt.show()
    fig.savefig(f"output/{title}_distribute.png")

    # 固有ベクトルを取得する
    component = pd.DataFrame(pcaer.components_, index=[f"PC{x+1}"
                                                     for x in range(2)],
    columns=data.columns[:-1])
    print(f"component:\n{component.head()}")

    component.to_csv(f'output/{title}_component.csv', index=True)
    # 固有ベクトルの第一主成分、第二主成分の寄与度を見る
    fig = plt.figure(figsize=(6, 6))
    for x_axis, y_axis, name in zip(pcaer.components_[0], pcaer.components_[1], data.columns[:-1]):
        plt.text(x_axis, y_axis, name)
    plt.scatter(pcaer.components_[0], pcaer.components_[1], alpha=0.8)

    plt.grid()
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title(f"{title}_heatvector")
    plt.show()
    fig.savefig(f"output/{title}_heatvector.png")
