import numpy as np
import pandas as pd

# --- Generazione dataset vendite ---
np.random.seed(42)

# 1 mese
inizio = "2025-11-01"
fine = "2025-11-30"

citta = ["Roma", "Milano", "Torino"]
prodotti = ["Prodotto A", "Prodotto B", "Prodotto C"]

num_righe = 300

# Array di date giornaliere nel mese di novembre
dates = pd.date_range(start=inizio, end=fine, freq="D") # D = 'Day'

data = {
    "Data": np.random.choice(dates, size=num_righe),
    "Città": np.random.choice(citta, size=num_righe),
    "Prodotto": np.random.choice(prodotti, size=num_righe),
    "Vendite in €": np.round(np.random.uniform(10.0, 500.0, size=num_righe), 2) # Uso np.round(x,2) così mi arrotonda i float x a 2 cifre decimali
}

df = pd.DataFrame(data)
df = df.sort_values("Data").reset_index(drop=True) # Ordino le righe per data e resetto l'indice

# Salvo il DF in un file CSV
csv_path = "CORSO PYTHON/12. Gio 27-11-2025/Analisi Vendite Fittizie/sales_data.csv"
df.to_csv(csv_path, index=False)
print("CSV salvato in:", csv_path)

# ---------------------------------------------------------------------------

# Creo tabella pivot
pivot = pd.pivot_table(df, index="Città", columns="Prodotto", values="Vendite in €", aggfunc="mean")

# Sommo tutte le vendite per ogni prodotto
grouped = df.groupby("Prodotto", as_index=True)["Vendite in €"].sum()

print("\nPivot (vendite medie in €):")
print(pivot.round(2))

print("\nVendite totali per prodotto in €:")
print(grouped.round(2))