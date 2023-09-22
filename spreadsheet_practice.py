import pandas as pd
import os

distance = float(input("Give in km the distance from the surface of each planet: "))

spreadsheet = pd.read_excel("spreadsheet.xlsx")
spreadsheet['Gravitational Acceleration (m/s^2)'] =  (spreadsheet['masses (kg)'] * 6.67*10**-11) / ((distance + spreadsheet['diameters (km)'] / 2)**2)
print(spreadsheet)

