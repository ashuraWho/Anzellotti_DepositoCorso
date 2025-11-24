import numpy as np

# Array: [0,49] + 50 casuali in [49,101]
base = np.arange(50) # [0,49]
extra = np.random.randint(49, 102, size=50) # 50 casuali in [49,101]
arr = np.concatenate([base, extra]) # Vado a concatenare i due "intervalli"

print("--- Pre-conversione a float64 ---")
print("Array:\n", arr)
print("dtype:", arr.dtype)
print("shape:", arr.shape)
print("\n")

# Modifico il dtype in float64
arr = arr.astype(np.float64)

print("--- Post-conversione a float64 ---")
print("dtype:", arr.dtype)
print("shape:", arr.shape)
print("\n")

# Slicing
primi_10 = arr[:10]
ultimi_7 = arr[-7:]
intervallo_5_20 = arr[5:20] # 20 escluso
ogni_4 = arr[::4]

# Modifico elementi
arr[10:15] = 999.0

# Fancy indexing
indice_elem = [0, 3, 7, 12, 25, 33, 48]
elem_selezionati = arr[indice_elem]

maschera = (arr % 2 == 0) # Ho su float, ma sono valori interi
pari = arr[maschera]

media = arr.mean()
maggiori_media = arr[arr > media]

# Stampe varie
print("--- Array originale (dopo le modifiche) ---")
print(arr)
print("\n")

# Sotto-array
print("--- Sotto-array ottenuti tramite slicing ---")
print("Primi 10 elementi:\n", primi_10, "\n")
print("Ultimi 7 elementi:\n", ultimi_7, "\n")
print("Elementi dall'indice 5 all'indice 20 (escluso 20):\n", intervallo_5_20, "\n")
print("Ogni quarto elemento dell'array:\n", ogni_4, "\n")

print("--- Fancy indexing ---")
print(f"Elementi in posizioni {indice_elem}:\n", elem_selezionati, "\n")
print("Tutti gli elementi pari:\n", pari, "\n")
print(f"Media dell'array: {media}\n")
print("Tutti gli elementi maggiori della media:\n", maggiori_media, "\n")