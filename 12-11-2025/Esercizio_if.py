print("\nEsercizio 1")
print("\nCreare una serie di condizioni una dentro l’altra che a fronte di un input per ogni if decidano se farti passare o no ( 3 livelli, fate un paragone con == )")
print()

# Primo livello: controllo nome utente
nome = input("Inserisci il tuo nome: ")

if nome == "Emanuele":
    # Secondo livello: controllo password
    password = input("Inserisci la password: ")
    
    if password == "123":
        # Terzo livello: controllo codice segreto
        codice = input("Inserisci il codice segreto: ")
        
        if codice == "UOVO":
            print("Accesso consentito.")
        else:
            print("Codice segreto errato")
    else:
        print("Password errata.")
else:
    print("Nome non riconosciuto.")
    
print("\nEsercizio 2")
print("\nAndare a creare un if con vari elif e un else finale che gestisca un menu per la selezione di un crud basilare (aggiungi rimuovi elimina)")
print()

# Stampa del menu
print("*****************")
print("*** MENU CRUD ***")
print("*****************")
print("0. Esci")
print("1. Aggiungi elemento")
print("2. Visualizza elementi")
print("3. Modifica elemento")
print("4. Rimuovi elemento")

# Input dell’utente
scelta = input("\nSeleziona un'opzione (0-4): ")

# Struttura di controllo
if scelta == "0":
    print("Hai selezionato: Esci")
elif scelta == "1":
    print("Hai selezionato: Aggiungi elemento")
elif scelta == "2":
    print("Hai selezionato: Visualizza elementi")
elif scelta == "3":
    print("Hai selezionato: Modifica elemento")
elif scelta == "4":
    print("Hai selezionato: Rimuovi elemento")
else:
    print("Scelta non valida.")
