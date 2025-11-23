ripetere = False

while ripetere == False:
    
    conteggio = int(input("\nInserisci un numero intero positivo: "))
    
    while conteggio < 0:
        print("Numero non valido. Riprova.")
        conteggio = int(input("Inserisci un numero intero positivo: "))
    
    print("\nConteggio alla rovescia:")
    for i in range(conteggio, 0, -1):
        print(i)
        
    ripetere_input = input("Vuoi ripetere il conteggio alla rovescia? (si per continuare): ")
    if ripetere_input.lower() == 'si':
        ripetere = False
    else:
        print("Uscita dal programma.")
        ripetere = True