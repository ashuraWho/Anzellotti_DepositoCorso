pari = [] # Dove vanno inseriti i numeri pari
primi = [] # Dove vanno inseriti i numeri primi

opzione = input("Vuoi inserire 5 numeri pari o primi? (pari/primi): ")
if opzione.lower() == 'primi':
    while primi.__len__() < 5:
        
        numero = int(input("\nInserisci un numero primo: "))

        # Controllo se il numero è primo
        if numero > 1:
            for i in range(2, int(numero**0.5) + 1):
                if (numero % i) == 0:
                    print("Numero non primo. Riprova.")
                    break
                else:
                    primi.append(numero)
        else:
            print("Numero non primo. Riprova.")

    primi.sort()
    print("\nHai inserito i seguenti numeri primi: ", primi)
    exit()

elif opzione.lower() == 'pari':
    while pari.__len__() < 5:
        
        numero = int(input("\nInserisci un numero pari: "))

        # Controllo se il numero è pari
        if numero % 2 == 0:
            pari.append(numero)
        else:
            print("Numero dispari o negativo. Riprova.")

    pari.sort()
    print("\nHai inserito i seguenti numeri pari: ", pari)

else:
    print("Opzione non valida. Uscita dal programma.")