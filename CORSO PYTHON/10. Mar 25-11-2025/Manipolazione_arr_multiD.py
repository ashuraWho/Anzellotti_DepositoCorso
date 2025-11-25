import numpy as np

matrice = np.arange(1, 26).reshape(5, 5) # Faccio l'array con arange e subito reshape per trasformarlo in matrice -> risparmio memoria
print("Matrice:\n", matrice)
print("\n")

seconda_colonna = matrice[:, 1]
print("Seconda colonna:\n", seconda_colonna)
print("\n")

terza_riga = matrice[2, :]
print("Terza riga:\n", terza_riga)
print("\n")

somma_diagonale = np.diag(matrice).sum()
print(f"Elementi della diagonale: {np.diag(matrice)}")
print(f"Somma: {somma_diagonale}")