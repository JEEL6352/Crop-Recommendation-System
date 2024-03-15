import pandas as pd
df=pd.read_csv("Crop_recommendation.csv")
print(df.isnull().sum())
df=df.dropna()
print(df.isnull().sum())
print(df.dtypes)
X=df.iloc[:,:-1]
y=df.iloc[:,-1]
X=X.to_numpy()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.75)

from sklearn.svm import SVC
model=SVC()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))
from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

import pickle
pickle.dump(model,open("model-svm-crop.pkl","wb"))

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))
from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

import pickle
pickle.dump(model,open("model-rf-crop.pkl","wb"))

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))
from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

import pickle
pickle.dump(model,open("model-KNN-crop.pkl","wb"))

from sklearn import tree
model=tree.DecisionTreeClassifier()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))
from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

import pickle
pickle.dump(model,open("model-dt-crop.pkl","wb"))

