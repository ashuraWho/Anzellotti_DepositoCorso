import pandas as pd

# ChatGPT mi ha creato il dataset 
data = {
    "Prodotto": ["Laptop", "Smartphone", "Tablet", "Laptop", "Smartphone", "Tablet", "Laptop", "Tablet"],
    "Quantità": [5, 10, 7, 3, 5, 2, 8, 4],
    "Prezzo Unitario": [1000, 500, 300, 1000, 500, 300, 1000, 300],
    "Città": ["Roma", "Milano", "Torino", "Roma", "Milano", "Torino", "Napoli", "Roma"]
}

df = pd.DataFrame(data)
print("\nDataset originale:\n", df)

# Aggiungo colonna "Totale Vendite"
df["Totale Vendite in €"] = df["Quantità"] * df["Prezzo Unitario"]
print("\nDataset con Totale Vendite in €:\n", df)

# Raggruppo per prodotto e calcolo totale vendite
vendite_per_prodotto = df.groupby("Prodotto")["Totale Vendite in €"].sum().reset_index()
# reset_index() trasforma l'indice del groupby in colonna -> così non mi dà problemi
print("\nTotale vendite per prodotto in €:\n", vendite_per_prodotto)

# Prodotto più venduto (quantità)
prodotto_piu_venduto = df.groupby("Prodotto")["Quantità"].sum().idxmax() # idxmax() restituisce l'indice con il valore massimo
quantita_massima = df.groupby("Prodotto")["Quantità"].sum().max() # Quantità massima venduta per quel prodotto
print(f"\nProdotto più venduto: {prodotto_piu_venduto} ({quantita_massima} unità)")

# Città con il maggior volume di vendite totali
citta_top = df.groupby("Città")["Totale Vendite in €"].sum().idxmax()
vendite_citta_top = df.groupby("Città")["Totale Vendite in €"].sum().max()
print(f"\nCittà con il maggior volume di vendite: {citta_top} ({vendite_citta_top}€)")

# Nuovo DF -> vendite > 1000€
df_grandi_vendite = df[df["Totale Vendite in €"] > 1000]
print("\nVendite superiori a 1000 €:\n", df_grandi_vendite)

# Ordino DF originale per Totale Vendite decrescente
df_ordinato = df.sort_values(by="Totale Vendite in €", ascending=False)
print("\nDataFrame ordinato per Totale Vendite in €:\n", df_ordinato)

# Numero di vendite per città
numero_vendite_per_citta = df["Città"].value_counts() # value_counts() conta quante volte ogni valore appare
print("\nNumero di vendite per città:\n", numero_vendite_per_citta)