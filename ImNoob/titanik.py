import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# import tensorflow as tf
# import tensorflow_decision_forests as tfdf

#kaggle tutorial titanic
#go linux

titanic_data = pd.read_csv(r"E:\python\udemy\titanic\train.csv")
titanic_test = pd.read_csv(r"E:\python\udemy\titanic\test.csv")

print(titanic_data)

y = titanic_data["Survived"]
feartures = ["Pclass", "Sex", "SibSp", "Parch"]

# def preprocess(df):
#     df = df.copy()

#     def normalize_name(x):
#         return " ".join([v.strip(",()[].\"'") for v in x.split(" ")])
    
#     def ticket_number(x):
#         return x.sprit(" ")[-1]

#     def ticket_item(x):
#         items = x.sprit(" ")
#         if len(items) == 1:
#             return "NONE"
#         return "_".join(items[0:-1])     
    
#     df["Name"]  = df["Name"].apply(normalize_name)
#     df["Ticket_Number"] = df["Ticket_Number"].apply(ticket_number)
#     df["Ticket_item"] = df["Ticket"].apply(ticket_item)
#     return df



# X = pd.get_dummies(titanic_data[feartures])
# X_test = pd.get_dummies(titanic_test[feartures])

# model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)

# model.fit(X,y)
# predictions = model.predict(X_test)

# output = pd.DataFrame({'PassengerId': titanic_test.PassengerId, 'Survived':predictions})

# output.to_csv('submission.csv', index=False)
print('Ok! submission was saved.')