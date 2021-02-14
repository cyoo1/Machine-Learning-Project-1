import pandas as pd
from sklearn import linear_model

import PySimpleGUI as sg

sg.theme("DarkBlue12")

sqft = sg.InputText()
beds = sg.InputText()
baths = sg.InputText()

layout = [[sg.Text("Am-Ko Painting Estimation Tool")], 
[sg.Text("Enter square footage of the house:"), sqft], 
[sg.Text("Enter the number of bedrooms:"), beds], 
[sg.Text("Enter number of bathrooms"), baths],
[sg.Button("Submit"), sg.Button("Cancel")] ]

windowScreen = sg.Window("Am-Ko Painting Cost Estimator", layout)

while True:
    event, values = windowScreen.read()
    if event == sg.WIN_CLOSED or sg.Button("Cancel"):
        break
        windowScreen.close()  
    elif event == sg.Button("Submit"):
        df = pd.read_csv("Machine Learning/Project1/BusinessData1.csv")
        X = df[['SqFt','Bed','Bath']]
        y = df[['Total']]
        regression = linear_model.LinearRegression()
        regression.fit(X, y)
        estimateHousePredict = regression.predict([[sqft,beds,baths]])

        layout2 = [[sg.Text("Estimated cost of painting:" + str(estimateHousePredict))], [sg.Button("Return Home")]]
        windowScreen2 = sg.Window("Am-Ko Painting Cost Estimator")

        while True:
            event2, value2 = windowScreen2.read()

            if event == sg.WIN_CLOSED or sg.Button("Return Home"):
                windowScreen2.close()
                windowScreen.read()
#still needs work on closing and reopening windows on button command and fix window size

 
