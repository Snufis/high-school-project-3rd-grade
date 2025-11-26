import numpy as np
import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')

def Czesc1():
    print(df.head())
    print(df.tail())

    print(df.columns)
    print(df.dtypes)



#Czesc1()
print(df.describe)