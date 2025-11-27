import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split # Per dividere i dati in train e test
from sklearn.preprocessing import MinMaxScaler # Per normalizzare i dati
from sklearn.linear_model import LogisticRegression # Modello di regressione logistica
from sklearn.metrics import accuracy_score, roc_auc_score # Metriche di valutazione

filename = input("Inserisci il nome del file CSV da caricare: ")
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

# ------------------------------------------------------

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

# ------------------------------------------------------

# --- PULIZIA DATI ---

# Rimuovo righe vuote
df = df.dropna(how="all")

# Valori numerici mancanti -> media della colonna
for col in df.select_dtypes(include=[np.number]).columns:
    df[col] = df[col].fillna(df[col].mean())

# Valori Churn mancanti -> "No"
df["Churn"] = df["Churn"].fillna("No")

# Valori anomali:
df["Età"] = df["Età"].apply(lambda x: np.nan if x < 0 else x) # Età negativa -> nan
df["Età"] = df["Età"].fillna(df["Età"].median())  #  nan -> mediana

# Tolgo valori tariffa anomali (es. < 0)
df["Tariffa_Mensile"] = df["Tariffa_Mensile"].clip(lower=0)

# ------------------------------------------------------

# --- ANALISI ESPLORATIVA DATI (EDA) ---

# Nuova colonna costo per GB -> no diviso 0
df["Costo_per_GB"] = df["Tariffa_Mensile"] / df["Dati_Consumati"].replace(0, np.nan)
df["Costo_per_GB"] = df["Costo_per_GB"].fillna(0)

# Groupby
print("\n--- MEDIA ATTRIBUTI PER CHURN ---")
print(df.groupby("Churn")[["Età", "Durata_Abonnamento", "Tariffa_Mensile"]].mean())

# Studio correlazione
print("\n--- CORRELAZIONI ---")
print(df.corr(numeric_only=True))

# ------------------------------------------------------

# --- PREPARAZIONE MODELLAZIONE ---

# Conversione Churn
df["Churn_Num"] = df["Churn"].map({"No": 0, "Si": 1, "Sì": 1}) # La gente può scrivere "Si" o "Sì"

# Valori non mappati? Metto a 0
df["Churn_Num"] = df["Churn_Num"].fillna(0)

# Seleziono le colonne numeriche per normalizzazione
colonne_numeriche = ["Età", "Durata_Abonnamento", "Tariffa_Mensile", "Dati_Consumati", "Servizio_Clienti_Contatti", "Costo_per_GB"]

# Inizializzo lo scaler MinMax
scaler = MinMaxScaler()

# Normalizzo le colonne
df[colonne_numeriche] = scaler.fit_transform(df[colonne_numeriche])

# ------------------------------------------------------

# --- MODELLAZIONE PREDITTIVA ---

# Variabili indipendenti (X) = tutte le colonne numeriche normalizzate
X = df[colonne_numeriche]

# Variabile dipendente (y) = churn numerico
y = df["Churn_Num"]

# Dividiamo in train e test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Inizializziamo la regressione logistica
model = LogisticRegression()

# Alleniamo il modello
model.fit(X_train, y_train)

# Predizioni sul test
y_pred = model.predict(X_test)

# Predizioni probabilistiche (necessarie per AUC)
y_prob = model.predict_proba(X_test)[:, 1]

# Calcoliamo l'accuratezza
accuracy = accuracy_score(y_test, y_pred)

# Calcoliamo l'AUC
auc = roc_auc_score(y_test, y_prob)

# Stampiamo i risultati
print("\n=== RISULTATI MODELLO ===")
print("Accuratezza:", accuracy)
print("AUC:", auc)