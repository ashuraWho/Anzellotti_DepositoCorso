# --------------------------------------------------------------
# ------------------- ESERCITAZIONE COMPLETA -------------------
# --------------------------------------------------------------

opzione = False

while not opzione:
    comando = input("\nScegli l'opzione: exit, start. ")

    match comando:
        case "exit":  # --- exit ---
            print("\nUscita dal programma.")
            opzione = True
            
        case "start":  # --- start ---
            print("\nAvvio dell'esercitazione completa.")
            
            continuo = True
            
            numeri = [] # Lista per memorizzare i numeri inseriti
            sum_pari = [] # Lista per la somma dei numeri pari
            sum_dispari = [] # Lista per la somma dei numeri dispari
            primo = [] # Lista per verificare se il numero è primo (True/False)
            
            lista = [numeri, sum_pari, sum_dispari, primo] # Lista di liste
            
            while continuo:
            
                n = int(input("\nInserisci un numero intero positivo: "))
                
                while n <= 0:
                    n = int(input("Per favore, inserisci un numero POSITIVO: "))
                
                numeri.append(n)

                # Stampa numeri da 1 a n pari
                print(f"\nNumeri pari da 1 a {n}:")
                for i in range(2, n+1, 2):
                    print(i)

                # Somma numeri pari da 1 a n
                somma_pari = sum(i for i in range(2, n+1, 2))
                print(f"\nLa somma dei numeri pari da 1 a {n} è: {somma_pari}")
                sum_pari.append(somma_pari)
                
                # Stampa numeri da 1 a n dispari
                print(f"\nNumeri dispari da 1 a {n}:")
                for i in range(1, n+1, 2):
                    print(i)
                    
                # Somma numeri dispari da 1 a n
                somma_dispari = sum(i for i in range(1, n+1, 2))
                print(f"\nLa somma dei numeri dispari da 1 a {n} è: {somma_dispari}")
                sum_dispari.append(somma_dispari)
                
                # Verifica se n è primo
                if n < 2:
                    print(f"\n{n} non è un numero primo.")
                    primo.append(False)
                else:
                    for i in range(2, int(n**0.5) + 1):
                        if n % i == 0:
                            print(f"\n{n} NON è un numero primo.")
                            primo.append(False)
                            break
                    else:
                        print(f"\n{n} è un numero primo.")
                        primo.append(True)
            
                continua_input = input("\nVuoi inserire un altro numero? (s/n): ").lower()
                if continua_input != 's':
                    continuo = False
                    
                    print("\nFine dell'esercitazione completa.")
                    print("\nRiepilogo dei numeri inseriti e delle loro proprietà:")
                    
                    nomi = ["Numeri", "Somme Pari", "Somme Dispari", "Primo?"] # Nomi delle liste

                    for i in range(len(lista)): # Primo ciclo sulle liste
                        print(f"\n{nomi[i]}:")  # Stampa il nome
                        
                        for valore in lista[i]: # Secondo ciclo dentro la sottolista
                            print(valore)

            for sottolista in lista: # Pulizia della memoria
                sottolista.clear()
            
        case _:
            print("\nComando non riconosciuto.")
            print("Per favore, inserisci 'exit' o 'start'.")