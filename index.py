import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os
os.makedirs("wykresy", exist_ok=True)
plt.rcParams['savefig.dpi'] = 300



df = pd.read_csv('StudentsPerformance.csv')
df['sredni wynik'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

def Czesc1():
    print("\n-pierwsze wiersze tabeli:\n",df.head())
    print("\n-ostatnie wiersze tabeli:\n",df.tail())

    print("\n-kolumny:\n",df.columns)
    print("\n-typy danych:\n",df.dtypes)

    print("\n-srednia:\n",df.mean(numeric_only=True))
    print("\n-mediana:\n",df.median(numeric_only=True)) #
    print("\n-min:\n",df.min(numeric_only=True))
    print("\n-max:\n",df.max(numeric_only=True))
    print("\n-wariancja:\n",df.var(numeric_only=True))
    print("\n-odchylenie standardowe:\n",df.std(numeric_only=True))

    print("\n-liczba niepustych wartości:\n",df.count(numeric_only=True))
    print("\n-liczba unikalnych wartości:\n",df.nunique())
    print("\n-najczesciej wystepująca wartość:\n",df.mode())
    print("\n-korelacja:\n",df.corr(numeric_only=True))

    print("\nBraki danych:\n",df.isnull().any().any())


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
    plt.figure()
    plt.hist(df['reading score'], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Wynik z czytania')
    plt.ylabel('Liczba uczniów')
    plt.title('Histogram wyników z czytania')
    plt.savefig("wykresy/histogram_reading.png")
    plt.close()


    plt.figure()
    plt.boxplot(
        [df['math score'], df['reading score'], df['writing score']],
        tick_labels=['Matematyka', 'Czytanie', 'Pisanie'],
        patch_artist=True,
        boxprops=dict(facecolor='lightgreen')
    )
    plt.ylabel('Wynik')
    plt.title('Porównanie wyników z trzech przedmiotów')
    plt.savefig("wykresy/boxplot_subjects.png")
    plt.close()


    plt.figure()
    df.groupby('gender')['sredni wynik'].mean().plot(kind='bar', color='orange')
    plt.ylabel('Średni wynik')
    plt.title('Średni wynik a płeć')
    plt.savefig("wykresy/bar_gender.png")
    plt.close()


    plt.figure()
    ax = df.groupby('test preparation course')['sredni wynik'].mean().plot(kind='bar', color='green')
    plt.ylabel('Średni wynik')
    plt.title('Średni wynik a kurs przygotowawczy')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    plt.savefig("wykresy/bar_course.png")
    plt.close()

    plt.figure()
    plt.scatter(
        df['math score'],
        df['reading score'],
        alpha=0.5,
        c=df['math score'],
        cmap='viridis'
    )
    plt.xlabel('Matematyka')
    plt.ylabel('Czytanie')
    plt.title('Zależność: matematyka vs czytanie')
    plt.colorbar(label='Wynik z matematyki')
    plt.savefig("wykresy/scatter_math_reading.png")
    plt.close()

    



def Czesc5():
        print("\n-wnioski:\n")
        print("\n-1.grupy które miały najlepsze srednie wyniki:\n",df.groupby('race/ethnicity')['sredni wynik'].mean().sort_values(ascending=False))
        print("\n-2.korelacja miedzy wynikami osob po kursie przygotowawczym vs bez:\n",df.groupby('test preparation course')['sredni wynik'].mean())

        print("3.Kurs przygotowawczy ma pozytywny wpływ na średnie wyniki studentów.")
        print("4.Grupy etniczne różnią się pod względem średnich wyników")
        print("5.Kobiety mają przeciętnie wyższe wyniki z czytania i pisania niż mężczyźni.")



    
Czesc1()
Czesc2()
Czesc3()
Czesc4()
Czesc5()








