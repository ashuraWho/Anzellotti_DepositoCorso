import numpy as np

# Creazione di un array 1D
arr = np.array([1, 2, 3, 4, 5])

# Creazione di un array 2D
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# ---------------------------------------------------------

# Creazione di un array
arr = np.array([1, 2, 3, 4, 5])

# Utilizzo di alcuni metodi
print("Forma dell'array:", arr.shape) # Output: (5,)
print("Dimensioni dell'array:", arr.ndim) # Output: 1
print("Tipo di dati:", arr.dtype) # Output: int64 (varia a seconda della piattaforma)
print("Numero di elementi:", arr.size) # Output: 5
print("Somma degli elementi:", arr.sum()) # Output: 15
print("Media degli elementi:", arr.mean()) # Output: 3.0
print("Valore massimo:", arr.max()) # Output: 5
print("Indice del valore massimo:", arr.argmax()) # Output: 4

# ---------------------------------------------------------

# Il dtype specifica il tipo di dati contenuti nell'array. -> Può essere int, float, bool, etc.
arr = np.array([1, 2, 3], dtype='int32')
print(arr.dtype) # Output: int32

# ---------------------------------------------------------

# La shape di un array indica le sue dimensioni. È una tupla che rappresenta il numero di elementi in ciascuna dimensione.
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape) # Output: (2, 3)