"""
ファイルから入力を受け取り、整形する
"""
import pandas as pd
from pandas.io.stata import StataReader
from sklearn.preprocessing import StandardScaler


def input_data(file: str):
    """
    ファイルから入力を受け取り、整形する

    Parameters
    ----------
    file : str
        入力ファイルのパス

        データはカンマ区切り

    Returns
    -------

    data : pandas.DataFrame
        入力データを標準化したデータ

        列は[`mean`,`median`,`max`,`min`,`membership_period`]
    """
    data_law = pd.read_csv(file)


    # 名義変数を削除する
    data_filt = data_law.drop(columns=["customer_id"])

    sc = StandardScaler()
    data = sc.fit_transform(data_filt)

    return data
