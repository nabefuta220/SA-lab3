"""クラスタ化したデータを分析する"""
import pandas as pd


def analyze_data(data: pd.DataFrame, file: str = None):
    """
    クラスタ化したデータを加工して出力する

    また、加工したデータをcsvファイルに出力する

    Paramters
    ---------
    data : pandas.DataFrame
        クラスタ化したデータ
        行は`mean`,`median`,`max`,`min`,`membership_period`,`cluster`の順
    file : str ,defalt = None
        出力するファイルの名前
    """
    #変数名を変更する
    data = data.rename(columns={'mean': "月内平均値", "median": "月内中央値",
                                "max": "月内最大値", "min": "月内最小値", "membership_period": "会員期間"})
    print(f"clusters:\n{data['cluster'].value_counts()}")
    #各クラスタごとで詳細を表示する
    describe = data.groupby('cluster').describe()

    if file is not None:
        data.to_csv(f"output/{file}_clustering.csv")
        describe.to_csv(f"output/{file}_describe.csv")
