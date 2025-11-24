import numpy as np

# 1. Creo un array di interi da 10 a 49
arr = np.arange(10, 50)
print("Array:", arr)

# 2. Verifico il tipo di dato dell'array
print("Tipo di dato iniziale:", arr.dtype)

# 3. Cambio il tipo di dato in float64
arr = arr.astype(np.float64)
print("Tipo di dato dopo la conversione:", arr.dtype)

# 4. Stampo la forma dell'array
print("Forma dell'array:", arr.shape)