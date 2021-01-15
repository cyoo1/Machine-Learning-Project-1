import pandas as pd
from sklearn import linear_model

df = pd.read_csv("Machine Learning/Project1/BusinessData1.csv")

X = df[['SqFt','Bed','Bath']]

y = df[['Total']]

regression = linear_model.LinearRegression()
regression.fit(X, y)

estimateHousePredict = regression.predict([[2954,4,3]])
print(estimateHousePredict)