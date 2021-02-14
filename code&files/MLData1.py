import pandas as pd
from sklearn import linear_model

import PySimpleGUI as sg

sg.Window(title = "GUI Test", layout = [[]], margins = (100,50).read())


sg.theme("DarkBlue12")

sqft = sg.InputText()
beds = sg.InputText()
baths = sg.InputText()

layout = [ [sg.Text("Enter square footage of the house:"), sqft], 
[sg.Text("Enter the number of bedrooms:"), beds], 
[sg.Text("Enter number of bathrooms"), baths] ]

windowScreen = sg.Window("Am-KoH Painting Cost Estimator", layout)

while True:
    event, values = windowScreen.read()
    if event == sg.WIN_CLOSED:
        break

windowScreen.close()   


df = pd.read_csv("Machine Learning/Project1/BusinessData1.csv")

X = df[['SqFt','Bed','Bath']]

y = df[['Total']]

regression = linear_model.LinearRegression()
regression.fit(X, y)

estimateHousePredict = regression.predict([[2954,4,3]])
print(estimateHousePredict)


#Find way to connect back end with UI? Research method in doing so
#Update CSV File