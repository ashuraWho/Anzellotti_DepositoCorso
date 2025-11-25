"""

    Il broadcasting è una potente
    funzione di NumPy che permette di
    eseguire operazioni aritmetiche su
    array di forme diverse.
    
"""

import numpy as np

arr = np.array([1, 2, 3, 4])
scalar = 10

# Broadcasting aggiunge lo scalare a ogni elemento dell'array
result = arr + scalar
print(result) # Output: [11 12 13 14]

# In questo esempio, lo scalare 10 viene broadcasted per avere la stessa dimensione dell'array arr.

"""
    
    --- Vantaggi del Broadcasting ---
    
    1. Efficienza: Evita la necessità di creare copie esplicite di array per
    adattarne le dimensioni, riducendo il consumo di memoria e migliorando le prestazioni.
    
    2. Semplicità: Rende il codice più leggibile e conciso, eliminando la
    necessità di scrivere loop espliciti per operazioni element-wise.

"""