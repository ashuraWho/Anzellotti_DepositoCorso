import numpy as np
import csv
import os

# Nomi colonne del dataset California Housing (default)
DEFAULT_COLS = ["MedInc","HouseAge","AveRooms","AveBedrms","Population","AveOccup","Latitude","Longitude","MedHouseVal"]

def load_california_csv(path: str, delimiter: str = ',', has_header: bool = True):
    
    """
    
        Carica il CSV e restituisce (clean_array, column_names).
            - Rimuove righe vuote e righe con NaN.
            - Se il file ha header lo usa; altrimenti usa DEFAULT_COLS.
            - Se il numero di colonne nel file non coincide con DEFAULT_COLS vengono create colonne generiche.
    
    """
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    # Leggo tutte le righe
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=delimiter)
        rows = list(reader)

    if len(rows) == 0:
        raise ValueError("Empty CSV file")

    # Rimuovo righe vuote
    rows = [r for r in rows if any(cell.strip() for cell in r)]
    if len(rows) == 0:
        raise ValueError("CSV contains only empty lines")

    # Determino l'header e l'indice di partenza dei dati
    if has_header:
        header = [c.strip() for c in rows[0]]
        
        # Se la riga header è numerica -> probabilmente non è header
        try:
            [float(x) for x in header]
            has_header = False # Header numerico -> consideriamo che non sia un header
            header = DEFAULT_COLS.copy() # Uso quello di default
            start_idx = 0
            
        except Exception:
            start_idx = 1
            if len(header) != len(DEFAULT_COLS):
                # Se ci sono meno colonne estendo il nome con generici
                if len(header) < len(DEFAULT_COLS):
                    header += [f"col{idx}" for idx in range(len(header), len(DEFAULT_COLS))]
    else:
        header = DEFAULT_COLS.copy() # Uso quello di default
        start_idx = 0


    numeric_rows = [] # Lista dove metto tutte le righe convertite in numeri (float o np.nan)
    
    for r in rows[start_idx:]: # Ciclo sulle righe del CSV
        r_clean = [cell.strip() for cell in r] # Rimuovo gli spazi iniziali e finali da ogni cella

        if len(r_clean) < len(header): # Se la riga ha meno colonne dell’header
            r_clean += [''] * (len(header) - len(r_clean)) # La completo con stringhe vuote -> tolgo errori di indice
            
        elif len(r_clean) > len(header): # Se la riga ha più colonne dell’header
            r_clean = r_clean[:len(header)] # Tronco il resto
            
        try:
            nums = [float(cell) if cell != '' else np.nan for cell in r_clean] # cella non vuota -> float | cella vuota -> nan
            numeric_rows.append(nums)
        except ValueError:
            numeric_rows.append([np.nan]*len(header)) # Riga corrotta: metto nan per tutta la riga (poi la rimuovo)

    arr = np.array(numeric_rows, dtype=float)

    # Prendo solo le righe dove tutti i valori sono numerici finiti
    clean = arr[np.isfinite(arr).all(axis=1)]

    return clean, header