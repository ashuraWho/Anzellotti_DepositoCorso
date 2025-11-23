# --------------------------------------------------------------
# --------------------------- MATRICI --------------------------
# --------------------------------------------------------------

# In Python, una matrice può essere rappresentata come una lista di liste,
# in cui ogni lista interna rappresenta una riga della matrice. 

# Questa rappresentazione permette di creare matrici di dimensioni arbitrarie
# e di accedere agli elementi utilizzando gli indici delle righe e delle colonne.

matrice = [
    
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    
]

# Possiamo accedere agli elementi utilizzando gli indici delle righe e delle colonne
elemento = matrice[0][1] # Prima riga, seconda colonna
print(elemento) # Output: 2

# Puoi anche iterare sugli elementi di una matrice utilizzando i cicli for, sia per le righe che per le colonne.
for riga in matrice:
    for elemento in riga:
        print(elemento) # Questa iterazione stamperebbe tutti gli elementi della matrice uno per uno.
