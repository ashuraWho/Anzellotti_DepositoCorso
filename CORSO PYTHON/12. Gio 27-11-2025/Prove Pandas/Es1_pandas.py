# --- PANDAS ---

# Pandas è il core per la PRE-ANALISI e la PULIZIA dei dati
# Riprende il concetto di Numpy di OPERAZIONE VETTORILE, invece l'array è completamente morto

# -> Pandas introduce due strutture dati fondamentali: DataFrame e Series.

#   (1) DataFrame:
#           Una struttura dati 2D simile a un foglio di calcolo o a una tabella SQL.
#           È composto da righe e colonne, dove ogni colonna può contenere dati
#           di un tipo specifico (numerici, stringhe, booleani, etc.).
#           
#           -> è monotipizzato solo lungo le colonne, non nel complesso

#   (2) Series:
#           Una struttura dati 1D che può essere vista come una
#           colonna di un DataFrame. Ogni Series ha un solo tipo di dato.

# --------------------------------------------------------------------------------

# Esempio di Caricamento del File CSV
import pandas as pd

# Percorso del file CSV
file_path = 'CORSO PYTHON/12. Gio 27-11-2025/Prove Pandas/vendite.csv'

# Caricamento dei dati nel DataFrame
df = pd.read_csv(file_path)

# Mostra le prime 5 righe del DataFrame per controllo
print(df.head()) # Dentro la parentesi posso mettere quante righe voglio