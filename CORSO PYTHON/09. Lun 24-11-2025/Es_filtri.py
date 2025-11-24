"""

    filter() è una funzione integrata che consente di filtrare
    gli elementi di una sequenza (come una lista, una tupla o
    un insieme) utilizzando una funzione di filtro.
    
    La funzione di filtro è una funzione che accetta un argomento
    e restituisce True o False a seconda che l'elemento debba 
    essere incluso o escluso dalla sequenza risultante.

"""

def is_even(x): # è pari
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(is_even, numbers))
print(even_numbers) # Output: [2, 4, 6, 8, 10]

# ------------------------------------------------------------
print("\n")
# ------------------------------------------------------------

# ESERCIZIO

"""

    Andare a creare un filtro che controlli se elem x e elem x+1
    della lista sono superiori a elem x+2 della lista con gli ultimi
    numeri usare due volte quelli presenti tranne l'ultimo.

"""

numeri = [1, 8, 3, 55, 54, 6, 72, 0, 94, 190]

def somma_due_maggiore_del_terzo(x): # Funzione di filtro: prende un indice x
    return numeri[x] + numeri[x + 1] > numeri[x + 2]

indici = range(len(numeri) - 2) # In questo modo x+1 e x+2 esistono sempre

indici_validi = list(filter(somma_due_maggiore_del_terzo, indici))

gruppi_validi = [
    (numeri[i], numeri[i + 1], numeri[i + 2])
    for i in indici_validi
]

print("Indici che rispettano la condizione:", indici_validi)
print("Gruppi (x, x+1, x+2) validi:", gruppi_validi)