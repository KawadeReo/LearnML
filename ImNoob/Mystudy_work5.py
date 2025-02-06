import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

#Linux版　データの前処理(EDA)を練習　

#カラム名
#PassengerId(旅客ID), Survived(生存有無), Pclass(客室クラス), Name(名前), Sex(性別), Age(年齢), SibSp(兄弟と配偶者), Parch(両親と子供)
#Ticket(チケット), Fare(運賃), Cabin(キャビン), Embarked(寄港地)


titanic_data = pd.read_csv("/home/pota/titanic/train.csv")
titanic_test = pd.read_csv("/home/pota/titanic/test.csv")

print(titanic_data)

y = titanic_data["Survived"]
feartures = ["Pclass", "Sex", "SibSp", "Parch"]

def preprocess(df):
    df = df.copy()

    def normalize_name(x):
        return " ".join([v.strip(",()[].\"'") for v in x.split(" ")])
    
    def ticket_number(x):
        return x.sprit(" ")[-1]

    def ticket_item(x):
        items = x.sprit(" ")
        if len(items) == 1:
            return "NONE"
        return "_".join(items[0:-1])     
    
    df["Name"]  = df["Name"].apply(normalize_name)
    df["Ticket_Number"] = df["Ticket_Number"].apply(ticket_number)
    df["Ticket_item"] = df["Ticket"].apply(ticket_item)
    return df



X = pd.get_dummies(titanic_data[feartures])
X_test = pd.get_dummies(titanic_test[feartures])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)

model.fit(X,y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': titanic_test.PassengerId, 'Survived':predictions})

output.to_csv('submission.csv', index=False)
print('Ok! submission was saved.')