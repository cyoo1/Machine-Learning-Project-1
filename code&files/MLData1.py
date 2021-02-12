import pandas as pd
from sklearn import linear_model

import PySimpleGUI as sg

sg.Window(title = "GUI Test", layout = [[]], margins = (100,50).read())

df = pd.read_csv("Machine Learning/Project1/BusinessData1.csv")

X = df[['SqFt','Bed','Bath']]

y = df[['Total']]

regression = linear_model.LinearRegression()
regression.fit(X, y)

estimateHousePredict = regression.predict([[2954,4,3]])
print(estimateHousePredict)

#Find way to connect back end with UI? Research method in doing so
#Update CSV File