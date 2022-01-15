# 統計分析法 第三回レポート

## 実行環境

python3.9.9

- pipenv

(これ以降のモジュールは`pipenv update`でダウンロードできます)

- pandas(1.3.5)
- matplotlib (3.5.1)
- scikit-learn (1.0.2)

## 分析の流れについて

まず、ファイルからのデータを[src/input_data.py](src/input_data.py)の`input_data`メソッド内で`pandas.read_csv`メソッドを用いて`DataFrame`を作成し、その中で名義変数である`customer_id`を削除した。

また、それらのデータを正規化したものも作成した。

データをそれぞれの手法でクラスタリングした後、データの解析と表示を行った。

まず、[src/analyze.py](src/analyze.py)内の`analyze_data`関数内で変数名を変更したものと、各クラスタごとに統計情報をそれぞれcsvファイルに出力した。

また、[src/visilze.py](src/visilze.py)内の`plot_data`メソッドでデータと名義変数に主成分分析を行い、2次元上にプロットした。



## k-meansでの分析

`sklearn.cluster`内の`KMeans`メソッドを用いて行った。

ソースコードは[k-menas.py](k_means.py)である。

### 実行結果

k-means.pyの実行結果,k-meansでのクラスタの分布、変数の寄与率をそれぞれ出力1、図1,図2に示す。

出力1 : k-means.pyの出力結果

<!-- [[[cog
import cog
import subprocess
command = 'pipenv run python3 k_means.py'
cp = subprocess.run(command, encoding='utf-8',
                        stdout=subprocess.PIPE, shell=True,check=True)
cog.outl("\n```text")
cog.outl(f"$ {command}")
cog.outl(cp.stdout)
cog.outl("```")
    ]]] -->

```text
$ pipenv run python3 k_means.py
       mean  median  max  min  membership_period  cluster
0  4.833333     5.0    8    2                 47        1
1  5.083333     5.0    7    3                 47        1
2  4.583333     5.0    6    3                 47        1
3  4.833333     4.5    7    2                 47        1
4  3.916667     4.0    6    1                 47        1
clusters:
3    1332
1    1249
0     840
2     771
Name: cluster, dtype: int64
explained_varience_radio_ :[0.69042666 0.18937526]
compopnents :
[[ 0.53265024  0.51384531  0.44183117  0.47001365 -0.19005026]
 [-0.10971924 -0.14919798 -0.23674476  0.12782904 -0.94515253]]
mean :
[ 3.79679324e-16  1.35599759e-16 -5.42399035e-17 -1.08479807e-16
 -5.42399035e-17]
covariance :
[[ 1.13217687  0.90245414  0.78486328  0.80381952 -0.25182324]
 [ 0.90245414  1.07580128  0.76481806  0.77130299 -0.21233606]
 [ 0.78486328  0.76481806  0.87718191  0.65285429 -0.10603252]
 [ 0.80381952  0.77130299  0.65285429  0.93111606 -0.38075827]
 [-0.25182324 -0.21233606 -0.10603252 -0.38075827  0.98491692]]
component:
         mean    median       max       min  membership_period
PC1  0.532650  0.513845  0.441831  0.470014          -0.190050
PC2 -0.109719 -0.149198 -0.236745  0.127829          -0.945153

```

<!-- [[[end]]] -->


また、クラスタの分布の詳細、クラスタごとの統計の詳細は、それぞれ[output/k-means_clustering.csv](output/k-means_clustering.csv),[output/k-means_describe.csv](output/k-means_describe.csv)でみることができる。


![fig1](output/k-means_distribute.png)

図1 k-meansでのクラスタの分布

![fig2](output/k-means_heatvector.png)

図2 k-meansでの変数に対する主成分の寄与率


図2より、月内利用回数の平均値、中央値のPC1の値が大きく、利用期間のPC2の値が小さい。そのため、k-meansでの2つの主成分は順に利用回数の多い常連、利用期間が長い古参であると考えられる。

その上で図1を見ると、それぞれのクラスタは1から順に、長く利用しているがあまり利用していない客層、加入したばかりであまり利用していない客層、利用回数は少なくなく、利用期間も幅がある通常利用客、利用回数が多い常連層だと考えられる。

## 凝集型階層的クラスタリングでの分析

まず、`scipy.cluster.hierarchy`内の`linkage`メソッドを用いてテンドログラムを作成し、`scipy.cluster.hierarchy`内の`dendrogram`メソッドを用いてテンドログラムを表示した。

また、`linkage`メソッドの返り値は[`クラスタA`,`クラスタB`,`2つのクラスタ間の距離`,`いま時点での併合したクラスタに含まれるデータ数`]の2次元配列となり、これが併合される順番に格納されている。

今回行う3つのクラスタ間の計算方法は単調であることが保証されているため、最後から3番目の値をクラスタリングのしきい値とした。

その値を元に、`scipy.cluster.hierarchy`内の`fcluster`メソッドを用いてクラスタリングを行った。


ソースコードは[src/hierarchical_clustering.py](src/hierarchical_clustering.py)である。
