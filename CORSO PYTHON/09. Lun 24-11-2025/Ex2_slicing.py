import numpy as np

# Creo una matrice 6x6 con numeri interi casuali tra 1 e 100
mat = np.random.randint(1, 101, size=(6, 6))
print("Matrice originale 6x6: ", mat)

# Estraggo la sotto-matrice centrale 4x4
centrale = mat[1:5, 1:5] # Rimuovo la prima e ultima riga (idem per la colonna)
print("Sotto-matrice centrale 4x4: ", centrale)

# Inverto le righe della sotto-matrice estratta
invertita = centrale[::-1, :]
print("Matrice invertita (righe invertite): ", invertita)

# Estraggo la diagonale principale della matrice invertita
diagonale = np.diag(invertita)
print("\nDiagonale principale della matrice invertita:")

# Sostituisco i multipli di 3 con -1 nella matrice invertita
invertita_mod = invertita.copy()
invertita_mod[invertita_mod % 3 == 0] = -1
print("Matrice invertita con multipli di 3 sostituiti da -1: ", invertita_mod)