import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance.csv')
df['sredni wynik'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

def Czesc1():
    print("\n-pierwsze wiersze tabeli:\n",df.head())
    print("\n-ostatnie wiersze tabeli:\n",df.tail())

    print("\n-kolumny:\n",df.columns)
    print("\n-typy danych:\n",df.dtypes)

    print("\n-srednia:\n",df.mean(numeric_only=True))
    print("\n-mediana:\n",df.median(numeric_only=True))
    print("\n-min:\n",df.min(numeric_only=True))
    print("\n-max:\n",df.max(numeric_only=True))
    print("\n-wariancja:\n",df.var(numeric_only=True))
    print("\n-odchylenie standardowe:\n",df.std(numeric_only=True))

    print("\n-liczba niepustych wartości:\n",df.count(numeric_only=True))
    print("\n-liczba unikalnych wartości:\n",df.nunique())
    print("\n-najczesciej wystepująca wartość:\n",df.mode())
    print("\n-korelacja:\n",df.corr(numeric_only=True))

    a = df.isnull().values.any()

    if a == True:
        print("\n-Puste miejsca w tabeli: sa")

    else:
        print("\n-Puste miejsca w tabeli: nie ma")


def Czesc2():
    print("\n-wartosci dla kolumny lunch:\n",df.lunch)
    print("\n-wyniki z matmy,pisania i czytania",df[['math score','reading score','writing score']])
    
    wynik = df[df['math score'] > 90]
    print("\n-studenci z wynikiem z matmy wiekszym od 90:\n",wynik)

    wynik2 = df[(df['gender'] == 'female') & (df['reading score'] > 70)]
    print("\n-kobiety z wynikiem z czytania wiekszym od 70:\n",wynik2)


    df['matma vs srednia'] = np.where(
    df['math score'] > df['math score'].mean(),
    'wynik z matmy ponad srednia',
    'wynik z matmy ponizej sredniej')


def Czesc3():
    print("\n-porownanie wyników z matmy na podstawie płci:\n",df.groupby('gender')['math score'].mean())
    print("\n-porównanie średniej na podstawie kursu:\n",df.groupby('test preparation course')['sredni wynik'].mean())



def Czesc4():
    df['reading score'].hist(bins=20)
    plt.xlabel('Wynik z czytania')
    plt.ylabel('Liczba studentów')
    plt.title('Histogram wyników z czytania')
    plt.show()

    #plt.boxplot([df['math score'], df['writing score'], df['reading score']], labels=['Math Score', 'Writing Score', 'Reading Score'])
    #plt.ylabel('Wyniki')
    #plt.title('Boxplot wyników z matmy, pisania i czytania')
   #plt.show()

    #for column in ['math score', 'reading score', 'writing score']:
        #plt.scatter(df.index, df[column], alpha=0.5)
        #plt.xlabel('Indeks studenta')
        #plt.ylabel(column)
        #plt.title(f'Scatter plot wyników z {column}')
        #plt.show()
    






Czesc4()

