print("\n************************")
print("*** SISTEMA DI LOGIN ***")
print("************************")

login = ["admin", "1234"] # Credenziali di accesso predefinite
utente = []  # Lista per memorizzare le credenziali inserite dall'utente

nome = input("\nInserisci il nome utente: ")
password = input("Inserisci la password: ")

utente.append(nome)
utente.append(password)

if utente[0] == login[0] and utente[1] == login[1]:
    print("\nAccesso consentito.")
    print("\nOra scegli una domanda segreta:")
    print("1. Qual è il tuo animale preferito?")
    print("2. Qual è il tuo colore preferito?")
    
    selezione = input("\nSeleziona 1 o 2: ")
    
    if selezione == "1":
        animale = input("Qual è il tuo animale preferito? ")
        login.append(animale)
    elif selezione == "2":
        colore = input("Qual è il tuo colore preferito? ")
        login.append(colore)
    else:
        print("Scelta non valida.")
        
    print("\nCredenziali salvate: ", login)

    print("\nVuoi cambiare un dato di accesso?")
    print("0. No")
    print("1. Cambia nome utente")
    print("2. Cambia password")
    print("3. Cambia risposta alla domanda segreta")
    
    scelta = input("\nSeleziona 0, 1, 2 o 3: ")
    
    if scelta == "0":
        print("Nessuna modifica effettuata.")
        
    elif scelta == "1":
        nuovo_nome = input("\nInserisci il nuovo nome utente: ")
        login[0] = nuovo_nome
        print("Nome utente aggiornato.")
        print("\nCredenziali aggiornate: ", login)
        
    elif scelta == "2":
        nuova_password = input("\nInserisci la nuova password: ")
        login[1] = nuova_password
        print("Password aggiornata.")
        print("\nCredenziali aggiornate: ", login)
        
    elif scelta == "3": 
        if len(login) > 2:
            nuova_domanda = input("\nInserisci la nuova risposta alla domanda segreta: ")
            login[2] = nuova_domanda
            print("Domanda segreta aggiornata.")
            print("\nCredenziali aggiornate: ", login)
        else:
            print("Errore: non è stata ancora impostata una domanda segreta.")
        
    else:
        print("Scelta non valida.")
            
else:
    print("\nAccesso negato. Nome utente o password errati.")
