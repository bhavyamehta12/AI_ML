# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.tree import DecisionTreeClassifier,plot_tree

# df= pd.read_csv("diabetes.csv");

# x=df.drop("label",axis=1)
# y=df["label"]

# model = DecisionTreeClassifier(
#     max_depth=3,
#     random_state=42
# )
# model.fit(x,y)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

df = pd.read_csv("diabetes.csv")
x=df.drop("label",axis=1)
y=df["label"]

X_train,X_test,y_train,y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model= DecisionTreeClassifier(random_state=42)
model.fit(X_train,y_train)

y_pred=model.predict(X_test)\

plt.figure(figsize=(9,8))
