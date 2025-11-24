import numpy as np

# Creo un array 1D di 20 interi casuali da 10 a 50
arr = np.random.randint(10, 51, size=20)
print("Array: ", arr)

# Estraggo i primi 10 elementi
primi_10 = arr[:10]
print("Primi 10 elementi: ", primi_10)

# Gli ultimi 5 elementi
ultimi_5 = arr[-5:]
print("Ultimi 5 elementi: ", ultimi_5)

# Gli elementi dall'indice 5 all'indice 15 (escluso)
da_5_a_15 = arr[5:15]
print("Da 5 a 15 (escluso): ", da_5_a_15)

# Ogni terzo elemento
ogni_tre = arr[::3]
print("Ogni terzo elemento: ", ogni_tre)

# Modifico gli elementi dall'indice 5 all'indice 10 (escluso)
arr[5:10] = 42
print("Array modificato: ", arr) # -> Lo slicing modifica direttamente l’array originale

# --------------------------------------------

# Creo una matrice 5x6 di numeri interi casuali tra 10 e 50
mat = np.random.randint(10, 51, size=(5, 6))
print("Matrice: ", mat)

# Estraggo le prime 3 righe
prime_3_righe = mat[:3, :]
print("Prime 3 righe: ", prime_3_righe)

# Le ultime 2 colonne
ultime_2_colonne = mat[:, -2:]
print("Ultime 2 colonne: ", ultime_2_colonne)

# Gli elementi dalle righe 1 a 4 (esclusa 4) e dalle colonne 2 a 5 (esclusa 5)
sotto_matrice = mat[1:4, 2:5]
print("Sotto-matrice (righe 1-4 e colonne 2-5): ", sotto_matrice)

# Ogni 2 righe e ogni 2 colonne
ogni_2 = mat[::2, ::2]
print("Ogni 2 righe e 2 colonne:", ogni_2)

# Imposto a 42 gli elementi dalle righe 2 a 4 (esclusa 4) e dalle colonne 1 a 3 (esclusa 3)
mat[2:4, 1:3] = 42
print("Matrice modificata: ",mat)