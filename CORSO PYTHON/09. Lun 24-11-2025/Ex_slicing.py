import numpy as np

# Creo un array 1D di 20 interi casuali da 10 a 50
arr = np.random.randint(10, 51, size=20)
print("Array: ", arr)

# I primi 10 elementi
primi_10 = arr[:10]
print("Primi 10 elementi: ", primi_10)

# Gli ultimi 5 elementi
ultimi_5 = arr[-5:]
print("Ultimi 5 elementi: ", ultimi_5)

# EGli elementi dall'indice 5 all'indice 15 (escluso)
da_5_a_15 = arr[5:15]
print("Da 5 a 15 (escluso): ", da_5_a_15)

# Ogni terzo elemento
ogni_tre = arr[::3]
print("Ogni terzo elemento: ", ogni_tre)

# Modifico gli elementi dall'indice 5 all'indice 10 (escluso)
arr[5:10] = 42
print("Array modificato: ", arr)