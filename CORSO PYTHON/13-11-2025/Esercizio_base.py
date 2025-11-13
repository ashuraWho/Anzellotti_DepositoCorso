# --------------------------------------------------------------
# -------------- NUMERI PARI e DISPARI o SEQUENZA --------------
# --------------------------------------------------------------

scelta = False

while not scelta:
    comando = input("Inserisci un: numero, stringa o esci: ")

    match comando:
        case "numero":  # --- PARI / DISPARI ---
            print("\nAvvio del programma.")
            
            numero = int(input("\nInserisci un numero intero: "))
            if numero % 2 == 0:
                print(f"Il numero {numero} è PARI.")
            else:
                print(f"Il numero {numero} è DISPARI.")
            
        case "stringa": # --- STRINGA ---
            print("\nAvvio del programma.")
            
            stringa = input("\nInserisci una stringa: ")
            print(f"Hai inserito la stringa: {stringa}")
            
            print("Il numero di caratteri nella stringa è:", len(stringa))
            if len(stringa) % 2 == 0:
                print(f"Il numero di caratteri è PARI.")
            else:
                print(f"Il numero di caratteri è DISPARI.")
            
        case "esci":   # --- ESCI ---
            print("\nUscita dal programma.")
            scelta = True
            
        case _:
            print("\nComando non riconosciuto.")
            print("Per favore, inserisci 'numero', 'stringa' o 'esci'.")