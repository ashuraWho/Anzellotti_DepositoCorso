import numpy as np

arr1 = np.linspace(0, 1, 12) # Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace
print(arr1)
print("\n")

mat1 = arr1.reshape((3, 4)) # Cambia la forma dell'array a una matrice 3x4
print(mat1)
print("\n")

mat2 = np.random.rand(3, 4) # Genera una matrice 3x4 di numeri casuali tra 0 e 1
print(mat2)
print("\n")

# Calcola e stampa la somma degli elementi di entrambe le matrici
sum1 = np.sum(mat1)
print(sum1)
print("\n")

sum2 = np.sum(mat2)
print(sum2)