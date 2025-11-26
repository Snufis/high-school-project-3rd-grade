import numpy as np
import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')

def Czesc1():
    print("pierwsze wiersze tabeli:\n",df.head())
    print("ostatnie wiersze tabeli:\n",df.tail())

    print("kolumny:\n",df.columns)
    print("typy danych:\n",df.dtypes)

    print("srednia:\n",df.mean(numeric_only=True))
    print("mediana:\n",df.median(numeric_only=True))
    print("min:\n",df.min(numeric_only=True))
    print("max:\n",df.max(numeric_only=True))
    print("wariancja:\n",df.var(numeric_only=True))
    print("odchylenie standardowe:\n",df.std(numeric_only=True))

    print("liczba niepustych wartości:\n",df.count(numeric_only=True))
    print("liczba unikalnych wartości:\n",df.nunique())
    print("najczesciej wystepująca wartość:\n",df.mode())
    print("korelacja:\n",df.corr(numeric_only=True))

    a = df.isnull().values.any()

    if a == True:
        print("są puste miejsca w tabeli")

    else:
        print("nie ma pustych miejsc w tabeli")




Czesc1()