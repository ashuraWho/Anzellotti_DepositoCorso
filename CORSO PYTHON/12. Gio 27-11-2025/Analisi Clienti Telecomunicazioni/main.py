import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler # Per normalizzare i dati

"""
    Il file CSV che importo lo ha generato l'AI.
"""

filename = input("\nInserisci il nome del file CSV da caricare: ")
path = "CORSO PYTHON/12. Gio 27-11-2025/Analisi Clienti Telecomunicazioni/"
filepath = os.path.join(path, filename)

"""
    File CSV:
        • ID_Cliente: Identificativo unico per ogni cliente
        • Età: Età del cliente
        • Durata_Abonnamento: Quanti mesi il cliente è stato abbonato
        • Tariffa_Mensile: Quanto il cliente paga al mese
        • Dati_Consumati: GB di dati consumati al mese
        • Servizio_Clienti_Contatti: Quante volte il cliente ha contattato il servizio clienti
        • Churn: Se il cliente ha lasciato la compagnia
"""
print("\n------------------------------------------------------")

# --- CARICO DATI ---

df = pd.read_csv(filepath)

# Info DF
print("\n--- INFO DEL DATASET ---")
print(df.info())

# Descrizione statistica per colonne numeriche
print("\n--- DESCRIZIONE STATISTICA ---")
print(df.describe())

# Conteggi Churn -> se il cliente ha lasciato la compagnia
print("\n--- CHURN ---")
print(df["Churn"].value_counts())

# Stampo anteprima
print("\n--- PRIME 5 RIGHE ---")
print(df.head())

print("\n------------------------------------------------------")

# --- PULIZIA DATI ---

# Rimuovo righe vuote
df = df.dropna(how="all")

# Valori numerici mancanti -> media della colonna
for col in df.select_dtypes(include=[np.number]).columns: # Scorro solo le colonne numeriche
    df[col] = df[col].fillna(df[col].mean())

# Pulisco il Churn
def pulisci_churn(val):
    if val is None:
        return "No" # Valori mancanti
    
    v = str(val).strip().lower() # Tolgo spazi e metto minuscolo
    
    # Valori validi
    if v in ["si", "sì", "sì'", "sı", "yes", "y"]:
        return "Si"
    
    if v in ["no", "0", "n", "nope"]:
        return "No" 
    
    # Tutto ciò che è sporco -> assumo "No"
    return "No"

# Pulisco
df["Churn"] = df["Churn"].apply(pulisci_churn)

# Valori anomali:
df["Età"] = df["Età"].apply(lambda x: np.nan if x < 16 or x > 100 else x) # -> nan (uso la lambda function)
df["Età"] = df["Età"].fillna(df["Età"].median())  #  nan -> mediana

# Tolgo valori tariffa anomali
df["Tariffa_Mensile"] = df["Tariffa_Mensile"].clip(lower=0) # Porto a 0 i valori negativi

# Info DF
print("\n--- INFO DATASET PULITO ---")
print(df.info())

# Descrizione statistica per colonne numeriche
print("\n--- DESCRIZIONE STATISTICA PULITA ---")
print(df.describe())

# Conteggi Churn -> se il cliente ha lasciato la compagnia
print("\n--- CHURN PULITO ---")
print(df["Churn"].value_counts())

# Stampo anteprima
print("\n--- PRIME 5 RIGHE PULITE ---")
print(df.head())

print("\n------------------------------------------------------")

# --- ANALISI ESPLORATIVA DATI (EDA) ---

# Nuova colonna costo per GB -> se ho nan da diviso 0 metto 0
df["Costo_per_GB"] = df["Tariffa_Mensile"] / df["Dati_Consumati"].replace(0, np.nan)
df["Costo_per_GB"] = df["Costo_per_GB"].fillna(0)

# Groupby
print("\n--- MEDIA ATTRIBUTI PER CHURN ---")
print(df.groupby("Churn")[["Età", "Durata_Abonnamento", "Tariffa_Mensile"]].mean())

# Studio correlazione
print("\n--- CORRELAZIONI ---")
print(df.corr(numeric_only=True)) # Calcolo correlazioni tra colonne numeriche

# Conversione Churn
df["Churn_Num"] = df["Churn"].map({"No": 0, "Si": 1}) # 0 = No, 1 = Si

# Calcolo la matrice completa
matrice_correlazione = df.corr(numeric_only=True) 
# Stampo le correlazioni con la variabile target 'Churn_Num'
print("\n--- CORRELAZIONE CON CHURN ---")
print(matrice_correlazione["Churn_Num"].sort_values(ascending=False))

print("\n------------------------------------------------------")

# --- PREPARAZIONE MODELLAZIONE ---

# Lista colonne numeriche da normalizzare
colonne_numeriche = ["Età", "Durata_Abonnamento", "Tariffa_Mensile", "Dati_Consumati", "Servizio_Clienti_Contatti", "Costo_per_GB"]

scaler = MinMaxScaler() # Normalizzo -> porto i valori tra 0 e 1

# Normalizzo le colonne
df[colonne_numeriche] = scaler.fit_transform(df[colonne_numeriche]) # scaler -> calcola min/max e trasforma i valori

# Stampo anteprima
print("\n--- PRIME 5 RIGHE NORMALIZZATE ---")
print(df.head())

print("\n------------------------------------------------------")