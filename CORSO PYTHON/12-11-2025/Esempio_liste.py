numeri = [1, 2, 3, 4, 5]
nomi = ["Alice", "Bob", "Charlie"]
misto = [1, "due", True, 4.5]

print(numeri[0])  # Stampa il primo elemento della lista numeri
print(numeri[2])   # Stampa il terzo elemento della lista numeri

numeri[2] = 10  # Modifica il terzo elemento della lista numeri
print(numeri) # Stampa la lista numeri modificata

numeri = [3, 1, 4, 2, 5]
print(len(numeri))  # Stampa la lunghezza della lista numeri
numeri.append(6)  # Aggiunge l'elemento 6 alla fine della lista numeri
print(numeri)  # Stampa la lista numeri dopo l'aggiunta
numeri.insert(2, 10)  # Inserisce l'elemento 10 alla posizione 2 nella lista numeri
print(numeri)  # Stampa la lista numeri dopo l'inserimento
numeri.remove(4)  # Rimuove l'elemento 4 dalla lista numeri
print(numeri)  # Stampa la lista numeri dopo la rimozione
numeri.sort()  # Ordina la lista numeri in ordine crescente
print(numeri)  # Stampa la lista numeri ordinata