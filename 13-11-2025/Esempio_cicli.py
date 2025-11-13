# Ciclo matematico
conteggio = 0

while conteggio < 5:
    print(conteggio)
    conteggio += 1
    
#Ciclo booleano
controllere = True

while controllere:
    scelta = input("Vuoi continuare? (si/no): ")
    
    if scelta.lower() == 'no':
        controllere = False
    else:
        print("Stai continuando")
        
# Ciclo for
numeri = [1, 2, 3, 4, 5]

for numero in numeri:
    print(numero) # Stampa ogni numero nella lista

# Ciclo for con range
for i in range(5):
    print(i) # Stampa numeri da 0 a 4

# Ciclo for con range e passo
for i in range(2, 10, 2):
    print(i) # Stampa numeri pari da 2 a 8