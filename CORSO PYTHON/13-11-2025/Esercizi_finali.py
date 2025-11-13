# --------------------------------------------------------------
# -------------------- ESERCITAZIONE FINALE --------------------
# --------------------------------------------------------------

opzione = False

while not opzione:
    comando = input("\nScegli l'esercizio: (0) esci, (1) ciclo while, (2) ciclo for o (3) ciclo range. Inserisci 0, 1, 2 o 3: ")

    match comando:
        case "0":  # --- esci ---
            print("\nUscita dal programma.")
            opzione = True
            
        case "1":  # --- ciclo while ---
            print("\nAvvio del ciclo while.")
            
            numero = 1
            lista_numeri = []
            
            while numero != 0:
                numero = int(input("\nInserisci numeri interi. Per terminare, inserisci 0."))
                lista_numeri.append(numero)
            
            print("\nHai inserito i seguenti numeri:")
            for n in lista_numeri:
                print(n)
                
            print("\nLa somma dei numeri inseriti è:", sum(lista_numeri))
            
        case "2": # --- ciclo for ---
            print("\nAvvio del ciclo for.")
            
            parola = input("\nInserisci una parola: ")
            print(f"Hai inserito la parola:")
            for lettera in parola:
                print(lettera)
            
        case "3":   # --- ciclo range ---
            print("\nAvvio del ciclo range.")
            
            N = int(input("\nInserisci un numero intero positivo: "))
            while N <= 0:
                N = int(input("Per favore, inserisci un numero POSITIVO: "))
            
            tipo = input("\nVuoi un passo intero o decimale? (int/dec): ").lower()
            while tipo not in ["int", "dec"]:
                tipo = input("Per favore, scegli 'int' o 'dec': ").lower()
            
            if tipo == "dec":
                step = float(input("\nInserisci il passo (decimale positivo): "))
                while step <= 0:
                    step = float(input("Per favore, inserisci un passo POSITIVO: "))
                    
                print(f"\nNumeri da 0 a {N} con passo {step}:")
                current = 0.0
                while current <= N:
                    print(f"{current:.2f}") # Stampa con 2 decimali
                    current += step
            else:
                step = int(input("\nInserisci il passo (intero positivo): "))
                while step <= 0:
                    step = int(input("Per favore, inserisci un passo POSITIVO: "))
                    
                print(f"\nNumeri da 0 a {N} con passo {step}:")
                for i in range(0, N + 1, step):
                    print(i)
        
        case _:
            print("\nComando non riconosciuto.")
            print("Per favore, inserisci '1', '2' o '3'.")