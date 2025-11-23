# --------------------------------------------------------------
# ---------------------------- TUPLE ---------------------------
# --------------------------------------------------------------

# Le tuple sono immutabili
punto = (3, 4)
colore_rgb = (255, 128, 0)
informazioni_persona = ("Alice", 25, "Femmina")

print(punto[0])  # Output: 3

punto = 3, 4 # Tuple packing
x, y = punto # Tuple unpacking
print(x, y)  # Output: 3 4

# --------------------------------------------------------------
# ------------------------ INSIEMI / SET -----------------------
# --------------------------------------------------------------

# I set (gli insiemi) sono collezioni di elementi unici
set1 = set([1, 2, 3, 4, 5])
set2 = {4, 5, 6, 7, 8}
set3 = {1, 2, 3, 3, 4, 4, 5}

# Nella stampa mostrerà solo elementi unici
print(set1)  # Output: {1, 2, 3, 4, 5}
print(set2)  # Output: {4, 5, 6, 7, 8}
print(set3)  # Output: {1, 2, 3, 4, 5}

# Operazioni sui set
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.union(set2))        # Unione: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) # Intersezione: {4, 5}
print(set1.difference(set2))   # Differenza: {1, 2, 3}
print(set1.symmetric_difference(set2)) # Differenza simmetrica: {1, 2, 3, 6, 7, 8}

# Aggiungere e rimuovere elementi
set1.add(6)
set1.discard(10) # Non genera errore se l'elemento non esiste
set1.remove(10) # Genera un errore se l'elemento non esiste

print(set1)  # Output: {1, 3, 4, 5, 6}

# len() per set: conta gli elementi
print(len(set1))  # Output: 5

# copy() per set: copia superficiale
set4 = set1.copy()
print(set4)  # Output: {1, 3, 4, 5, 6}

print(set2)  # Output: {4, 5, 6, 7, 8}
set2 = set1.copy()
print(set2)  # Output: {1, 3, 4, 5, 6}

# in per set: verifica appartenenza
print(3 in set1)  # Output: True
print(10 in set1) # Output: False