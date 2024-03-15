import pickle
N=25
P=50
K=16
T=30.0
H=90
PH=8.6
R=75

model=pickle.load(open("model-svm-crop.pkl","rb"))
print(model.predict([[N,P,K,T,H,PH,R]]))

model=pickle.load(open("model-rf-crop.pkl","rb"))
print(model.predict([[N,P,K,T,H,PH,R]]))

model=pickle.load(open("model-KNN-crop.pkl","rb"))
print(model.predict([[N,P,K,T,H,PH,R]]))

model=pickle.load(open("model-dt-crop.pkl","rb"))
print(model.predict([[N,P,K,T,H,PH,R]]))
