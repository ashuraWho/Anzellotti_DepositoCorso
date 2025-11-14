# --------------------------------------------------------------
# -------------------- ESERCITAZIONE GENERALE ------------------
# --------------------------------------------------------------

# Devi scrivere un programma che faccia quanto segue:
# 1. Chieda all'utente (tramite un match) se vuole eseguire l'esercitazione completa o uscire.
# 2. Prima di scegliere bisogna spiegare brevemente cosa fa il programma.
# 3. Il programma, se l'utente sceglie di eseguire l'esercitazione completa, deve:
#    a. Chiedere all'utente di registrarsi con un nome utente e una password tramite una funzione.
#    b. Si può anche sceglere di impostare una password random per l'utente se non vuole crearne una propria.
#    c. Dopo la registrazione, il programma deve stampare il nome e la password (o la password generata) e chiedere conferma.
#    d. Dopo il login, il programma deve chiedere all'utente di inserire i nomi, il lavoro e l'età di 3 persone in una funzione del punto (e).
#    e. Tutti i dati inseriti devono essere memorizzati in una lista al nella funzione.
#    f. Infine, il programma deve stampare tutti i dati inseriti in un formato leggibile.
# 4. Il programma deve gestire eventuali errori di input (ad esempio, età non numerica) tramite cicli e condizioni.
# 5. Alla fine, il programma deve chiedere all'utente se vuole eseguire di nuovo l'esercitazione completa o uscire.

# --------------------------------------------------------------

# IMPORTAZIONI
import random # Importazione del modulo random

# FUNZIONI
def login(): # funzione per il login: Esegue la registrazione/login e restituisce (nickname, password).
    nickname = input("Inserisci il tuo nickname: ")
    
    pdw_random = input("Vuoi una password generata casualmente? (sì/no): ").lower()
    while pdw_random not in ['sì', 'no', 'si']:
        pdw_random = input("Per favore, rispondi con 'sì' o 'no': ").lower()
    
    if pdw_random == 'sì' or pdw_random == 'si': # Generazione password casuale
        caratteri = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()" # Caratteri possibili
        password = '' # Inizializzazione della password vuota
        for _ in range(10): # Lunghezza della password
            password += random.choice(caratteri) # Aggiunta di un carattere casuale
    else:
        password = input("Inserisci la tua password: ")
    
    print(f"\nRegistrazione completata!\nNickname: {nickname}\nPassword: {password}")
    
    return nickname, password
    
# --------------------------------------------------------------

# Chiede i dati di N colleghi e restituisce una lista
def people(): # funzione per i dati personali
    lista = [] # lista dei colleghi e i loro dati
    
    # Chiedere quanti colleghi inserire
    while True:
        try:
            num_colleghi = int(input("\nQuanti colleghi vuoi inserire? "))
            if num_colleghi > 0:
                break
            else:
                print("Errore: devi inserire almeno un collega. Riprova.")
        except ValueError:
            print("Errore: devi inserire un numero valido. Riprova.")
    
    for i in range(num_colleghi):
        nome = input(f"\nOra inserisci il nome del collega {i+1}: ")
        lavoro = input(f"Ora inserisci il lavoro del collega {i+1}: ")
        
        # Gestione errori per l'età
        while True:
            try:
                eta = int(input(f"Ora inserisci l'età del collega {i+1}: "))
                break
            except ValueError:
                print("Errore: l'età deve essere un numero. Riprova.")
                
        collega = [nome, lavoro, eta]  # Crea una nuova lista per ogni collega
        lista.append(collega)
        
    return lista
           
# --------------------------------------------------------------

uscita = False

while not uscita:
    print("\nBenvenuto all'esercitazione completa!")
    print("Questo programma ti guiderà attraverso la registrazione, il login e l'inserimento di dati personali.") # Spiegazione del programma
    
    comando = input("\nScegli l'opzione: exit, start. ")

    # match per scegliere l'opzione
    match comando:
        case "exit":  # --- exit ---
            print("\nUscita dal programma.")
            uscita = True
            
        case "start":  # --- start ---
            print("\nAvvio dell'esercitazione completa.")
            
            while True:
                login()
                conferma = input("\nConfermare nickname e password? (s/n) ")
                
                while conferma not in ['s', 'n']:
                    conferma = input("Per favore, rispondi con 's' o 'n': ").lower()

                if conferma == "s":
                    break
            
            lavoratori = people()
            nomi = ["Nome", "Lavoro", "Età"]

            # Stampa intestazione
            print(f"\n{nomi[0]:<15} {nomi[1]:<15} {nomi[2]:<5}")
            print("-" * 40)

            # Ciclo su ogni lavoratore
            for collega in lavoratori:
                nome, lavoro, eta = collega
                print(f"{nome:<15} {lavoro:<15} {eta:<5}")

            # Ripetere il tutto?
            risposta = input("\nVuoi riprovare? (si per continuare): ").lower()
            if risposta != 'si':
                uscita = True
                print("\nFine dell'esercitazione completa.")
                    
                for sottolista in lavoratori: # Pulizia della memoria
                    sottolista.clear()
            
        case _:
            print("\nComando non riconosciuto.")
            print("Per favore, inserisci 'exit' o 'start'.")