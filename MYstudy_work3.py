import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.inspection import PartialDependenceDisplay


file_path = r"E:\python\udemy\study\valocom.csv"    #valoのコンペティティブの戦績データ


# pandasでCSVを読み込む
valo_data = pd.read_csv(file_path)
x = valo_data.loc[:,["ACS","K","D","A","DDA","HS","FK","FD","MK"]]   #ACS,DDA,KASTのデータのみ抜き出し　特徴量
t = valo_data.loc[:,["WIN"]]    #勝敗のみデータ 正解データ

# print(x)
# print(t)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,t,test_size=0.3,random_state=3)   #データの分割

from sklearn.linear_model import LogisticRegression #ロジスティクス回帰

model = LogisticRegression()

model.fit(x_train,y_train.values.ravel())  #学習

print(model.coef_)  #重みをprint

model_score = model.score(x_test,y_test)    #score%

# model_score = model.predict_proba(x_test) #負け・勝ち率の計算

print(model_score)    #表示


# PartialDependenceDisplay.from_estimator(
#     estimator=model,
#     X=x_train,
#     features=[0,1,2],  # 各特徴量ごとにプロット
#     kind='average'
# )


# # sns.pairplot(data=valo_data, vars=["ACS","DDA","KAST"], hue="WIN")
# plt.show()

# print(model_score.ACS > 300 & model_score.WIN == 0)
