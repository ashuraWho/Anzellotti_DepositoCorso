import numpy as np

# La funzione linspace genera un array di numeri equidistanti tra un
# valore iniziale e uno finale.

arr = np.linspace(0, 1, 5)
print(arr) # Output: [0. 0.25 0.5 0.75 1. ]

# ------------------------------------------------------------------

# Il modulo random di NumPy permette di generare array di numeri casuali.

random_arr = np.random.rand(3, 3) # Matrice 3x3 con valori casuali uniformi tra 0 e 1
print(random_arr)

# ------------------------------------------------------------------

arr = np.array([1, 2, 3, 4, 5])

sum_value = np.sum(arr)
print("Sum:", sum_value) # Output: Sum: 15

mean_value = np.mean(arr)
print("Mean:", mean_value) # Output: Mean: 3.0

std_value = np.std(arr)
print("Standard Deviation:", std_value) # Output: Standard Deviation: 1.4142135623730951