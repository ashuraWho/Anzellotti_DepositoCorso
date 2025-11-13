comando = input("\nSu cosa vuoi un esempio? (if, while/range, for, tutto): ").lower()

match comando:
    
    # -----------------
    # Esercizio 1
    # -----------------
    case "if":
        print("\nUtilizzo di if.")
        
        numero = int(input("\nInserisci un numero intero: "))
        if numero % 2 == 0:
            print(f"\n{numero} è un numero pari.")
        else:
            print(f"\n{numero} è un numero dispari.")

    # -----------------
    # Esercizio 2
    # -----------------
    case "while/range":
        print("\nUtilizzo di while e range.")
        
        continua = True
        
        while continua:
        
            numero = int(input("\nInserisci un numero intero positivo: "))
            
            while numero < 0:
                print("\nIl numero inserito è negativo. Riprova.")
                numero = int(input("Inserisci un numero intero positivo: "))
            
            print(f"\nStampa dei numeri da {numero} a 0:")
            for i in range(numero, -1, -1):
                print(i)
            
            interrompi = input("\nVuoi inserire un altro numero? (sì per ripetere): ").lower()
            if interrompi != 'sì':
                continua = False
                print("Uscita dal programma")
                
    # -----------------
    # Esercizio 3
    # -----------------
    case "for":
        print("\nUtilizzo di for.")
        
        numeri = []
        
        lunghezza = int(input("\nQuanti numeri vuoi inserire? "))
        for _ in range(lunghezza):
            n = float(input("Inserisci un numero: "))
            numeri.append(n)
        
        numeri.sort()
        print("\nI numeri inseriti sono: ", numeri)
        print("Il quadrato di ciascun numero è: ")
        for n in numeri:
            print(n ** 2)
            
    # -----------------
    # Esercizio 4
    # -----------------
    case "tutto":
        print("\nUtilizzo di if, while e for insieme.")
        
        numeri = []
        
        lunghezza = int(input("\nQuanti numeri vuoi inserire? "))
        for _ in range(lunghezza):
            n = float(input("Inserisci un numero: "))
            numeri.append(n)
        
        print("\nI numeri inseriti sono: ", numeri)
        
        # Numero massimo
        if len(numeri) == 0:
            massimo = None
        else:
            massimo = numeri[0]
            for n in numeri:
                if n > massimo:
                    massimo = n
        
        # Numeri in totale
        contatore = 0
        while contatore < len(numeri):
            contatore += 1
        
        # Stampare il risultatato
        if len(numeri) == 0:
            print("\nLista Vuota")
        else:
            print("\nNumero massimo:", massimo)
            print("\nNumero di elementi nella lista:", contatore)
        
    case _:
        print("\nComando non riconosciuto.")