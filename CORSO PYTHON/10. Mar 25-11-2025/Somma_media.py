import numpy as np

n = 15
rand_min = 1
rand_max = 100
arr_rand = np.random.random(n) * (rand_max - rand_min) + rand_min # Creo array con random

somma = np.sum(arr_rand)
media = np.mean(arr_rand)

print("Somma degli elementi:", somma)
print("Media degli elementi:", media)