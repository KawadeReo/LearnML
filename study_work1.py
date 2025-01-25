import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_california_housing

data_set = fetch_california_housing()

x,t = data_set.data , data_set.target   #x=数値データ t=答え
columns = data_set.feature_names    #カラム名をcolumnsに　カラム名＝特徴量

# print(type(x),x.shape)

df = pd.DataFrame(x,columns= columns)    #pandasのデータ形式にデータを変換

df['target'] = t    #targetというカラム名を追加して、t(答え)をデータに追加

# print(df)

x = df.drop(labels=['target'],axis = 1) #target以外のカラムをxに
t = df['target'].values #targetをyに

print(x)
print(t)

from sklearn.model_selection import train_test_split    #データと答えを分割するメソッド

x_train,x_test,t_train,t_test = train_test_split(x,t,test_size=0.3 ,random_state=0) #データと答えを分割するメソッド

from sklearn.linear_model import LinearRegression #重回帰分析のモデルのインポート

model = LinearRegression()  #インスタンスの作成

model.fit(x_train,t_train)  #学習

# print(model.coef_)  #パラメータが見れるらしい。なにそれ？　各カラムの重みらしい

# print('model_coef')
# print(model.coef_)
# print(model.coef_.shape)

# plt.figure(figsize=(10,7))
# plt.bar(x=columns,height = model.coef_)
# plt.show()        #モデルの重みの可視化 重みとは？
# print(model.intercept_) #バイアスの数値　なにそれ？

print(f'train score:{model.score(x_train,t_train)}')    #モデルの精度
print(f'train score:{model.score(x_test,t_test)}')    #モデルの精度 差が広いと過学習

y = model.predict(x_test)   #与えられた値に対して推論を行う(predict)
print(f'予測値: {y[3]}')    #予測結果　リストの最初
print(f'目標値:{t_test[3]}')    #正しい答え　リストの最初