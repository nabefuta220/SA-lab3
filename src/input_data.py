"""
ファイルから入力を受け取り、整形する
"""
import pandas as pd
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
    data_filt : pandas.DataFrame
        データから名義変数を取り除いたデータ

    data : numpy.ndarray
        入力データを標準化したデータ

        列は[`mean`,`median`,`max`,`min`,`membership_period`]
    """
    data_law = pd.read_csv(file)

    # 名義変数を削除する
    data_filt = data_law.drop(columns=["customer_id"])

    standarader = StandardScaler()
    data = standarader.fit_transform(data_filt)

    return data_filt, data
