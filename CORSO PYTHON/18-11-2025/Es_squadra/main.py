# --------------------------------------------------------------
# ------------------------ MAIN: SQUADRA -----------------------
# --------------------------------------------------------------

import squadra as sq

while True:
    print("\n--- Menu specifiche ---")
    print("(1) Giocatore")
    print("(2) Allenatore")
    print("(3) Assistente")
    print("(4) Esci")

    scelta = input("\nSeleziona un'opzione (1-4): ")

    match scelta:
        
        case "1":
            nome = input("\nNome giocatore: ")
            eta = int(input("Età giocatore: "))
            ruolo = input("Ruolo giocatore: ")
            numero_maglia = int(input("Numero maglia: "))
            giocatore = sq.Giocatore(nome, eta, ruolo, numero_maglia)
            giocatore.gioca_partita()
            
        case "2":
            nome = input("\nNome allenatore: ")
            eta = int(input("Età allenatore: "))
            anni_di_esperienza = int(input("Anni di esperienza: "))
            allenatore = sq.Allenatore(nome, eta, anni_di_esperienza)
            allenatore.dirige_allenamento()
                
        case "3":
            nome = input("\nNome assistente: ")
            eta = int(input("Età assistente: "))
            specializzazione = input("Specializzazione: ")
            assistente = sq.Assistente(nome, eta, specializzazione)
            assistente.supporta_team()
            
        case "4":
            print("\nChiusura programma.")
            break
        
        case _:
            print("\nScelta non valida, riprova.")