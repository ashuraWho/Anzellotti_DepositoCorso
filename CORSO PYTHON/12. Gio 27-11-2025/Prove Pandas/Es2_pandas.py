import pandas as pd

# Creazione di un DataFrame con dati di esempio
data = { # Dizionario
    'Nome': ['Alice','Bob','Carla'],
    'Età': [25, 30, 22],
    'Città': ['Roma','Milano','Napoli']
}

df = pd.DataFrame(data) # Lo convertiamo in DataFrame

# Stampa del DataFrame originale
print("DataFrame Originale:")
print(df)

# Selezione delle righe dove l'età è superiore a 23
df_older = df[df['Età'] > 23]

# Stampa delle righe selezionate
print("\nPersone con età superiore a 23 anni:")
print(df_older)

# Aggiungiamo una nuova colonna la persona maggiorenne
df['Maggiorenne'] = df['Età'] >= 18

# Stampa del DataFrame con la nuova colonna
print("\nDataFrame con colonna 'Maggiorenne':")
print(df)