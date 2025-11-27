import numpy as np
import pandas as pd
import os

"""

        Avendo iniziato con i dati di Titan, dove avevo come colonne "Age", "Cabin", "Embarked",
        quando ho implementato con i numeri autogenerati ho lasciato le stesse colonne
        e quindi non Nome, Eta, Citta, Salario.
        Avrei fatto la stessa cosa ma con Nome, Citta come stringhe e Eta, Salario come float,
        ma il procedimento sarebbe stato lo stesso di quanto fatto.

"""

opzione = input("\nPrendere i dat da 'Titanic Machine Learning from Disaster' o autogenerarli? (0-1) ")
if opzione == "0":
    # Ho preso i dati da: Titanic – Machine Learning from Disaster (colonne: Age, Cabin, Embarked)
    df = pd.read_csv("CORSO PYTHON/12. Gio 27-11-2025/Analisi Esplorativa Dati/train.csv", usecols=["Age", "Cabin", "Embarked"])
    
elif opzione == "1":
    np.random.seed(42)

    num = 50 # Voglio 200 persone
    
    # Genero Age, Cabin, Embarked
    age = np.random.randint(16, 85, num).astype(float) # Mi sembra che nan lo accetta solo se ho float e non int
    cabin = np.random.choice(["A10", "B20", "C30", "D40", None], num)
    embarked = np.random.choice(["C", "Q", "S", None], num)

    df = pd.DataFrame({
        "Age": age,
        "Cabin": cabin,
        "Embarked": embarked
    })

    # Metto nan su Age per 10 indici casuali ('replace=False' mi dice che non posso prendere lo stesso indice due volte)
    df.loc[np.random.choice(df.index, 10, replace=False), "Age"] = np.nan

    # Aggiungo 20 righe duplicate
    duplicati = df.sample(20)
    df = pd.concat([df, duplicati], ignore_index=True)
        
else:
    print("\nScegli 0 o 1.")
    exit()

# -----------------------------------------------------------

print("\nPrime 5 righe:")
print(df.head()) # In testa

print("\nUltime 5 righe:")
print(df.tail()) # In coda

# -----------------------------------------------------------

print("\nTipi di dati:")
print(df.dtypes)

# -----------------------------------------------------------

print("\nStatistiche descrittive:")
print("Media:", df["Age"].mean())
print("Mediana:", df["Age"].median())
print("Std:", df["Age"].std())

# -----------------------------------------------------------

# Rimuovo duplicati
df = df.drop_duplicates()

# --------------------- Valori mancanti ---------------------

# ETA -> li riempio con la mediana della colonna
df["Age"] = df["Age"].fillna(df["Age"].median())

# CABIN e EMBARKED -> stringhe -> metto 'Sconosciuto'
df["Cabin"] = df["Cabin"].fillna("Sconosciuto")
df["Embarked"] = df["Embarked"].fillna("Sconosciuto")

# -----------------------------------------------------------

# Nuova colonna "Categoria Età"
def categoria_eta(eta):
    if eta <= 18:
        return "Giovane"
    elif eta <= 65:
        return "Adulto"
    else:
        return "Senior"

df["Categoria Età"] = df["Age"].apply(categoria_eta)

# -----------------------------------------------------------

path = "CORSO PYTHON/12. Gio 27-11-2025/Analisi Esplorativa Dati/"

if opzione == 0:
    filename = os.path.join(path, "titanic_pulito.csv")
else:
    filename = os.path.join(path, "random_pulito.csv")

df.to_csv(filename, index=True, encoding="utf-8")

print(f"\nFile salvato come {filename}")