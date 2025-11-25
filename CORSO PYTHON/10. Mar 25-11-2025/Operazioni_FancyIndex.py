import numpy as np

n = 16 # Sarebbe 4x4
rand_min = 10
rand_max = 50

arr_rand = np.random.random(n) * (rand_max - rand_min) + rand_min
arr_rand = arr_rand.astype(int) # Li trasformo in interi
arr_rand = arr_rand.reshape(4, 4) # Forma 4x4

print("\nArray iniziale:\n", arr_rand)

# ----------------------------------------------------

# Per avere (0,1), (1,3), (2,2), (3,0) scrivo righe e colonne
righe = np.array([0, 1, 2, 3])
colonne = np.array([1, 3, 2, 0])

selezione = arr_rand[righe, colonne]

print("\nElementi selezionati con fancy indexing:")
print(selezione)

# ----------------------------------------------------

righe_dispari = arr_rand[[1, 3]]
print("\nRighe dispari (1 e 3):\n", righe_dispari)

# ----------------------------------------------------

print("\nArray dopo modifica degli elementi selezionati:\n", arr_rand + 10)