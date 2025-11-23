# --------------------------------------------------------------
# ---------------------- MAIN: MILITARE ------------------------
# --------------------------------------------------------------

import militare as mil

controllo = mil.ControlloMilitare()

while True:
    print("\n------------------- MENU -------------------")
    print("(1) Crea unità di Fanteria")
    print("(2) Crea unità di Artiglieria")
    print("(3) Crea unità di Cavalleria")
    print("(4) Crea unità di Supporto Logistico")
    print("(5) Crea unità di Ricognizione")
    print("(6) Mostra tutte le unità registrate")
    print("(7) Dettagli di una unità (con azione speciale)")
    print("(0) Esci")
    print("--------------------------------------------")

    scelta = input("Inserisci scelta: ")

    match scelta:
    
        # Creo unità
        case "1":
            nome = input("Nome unità: ")
            soldati = int(input("Numero soldati: "))
            trincee = int(input("Numero trincee: "))
            unita = mil.Fanteria(nome, soldati, trincee)
            controllo.registra_unita(unita)

        case "2":
            nome = input("Nome unità: ")
            soldati = int(input("Numero soldati: "))
            pezzi = int(input("Numero pezzi artiglieria: "))
            unita = mil.Artiglieria(nome, soldati, pezzi)
            controllo.registra_unita(unita)

        case "3":
            nome = input("Nome unità: ")
            soldati = int(input("Numero soldati: "))
            quadrante = input("Quadrante da esplorare: ")
            unita = mil.Cavalleria(nome, soldati, quadrante)
            controllo.registra_unita(unita)

        case "4":
            nome = input("Nome unità: ")
            soldati = int(input("Numero soldati: "))
            intervento = input("Tipo intervento (rifornimento/manutenzione): ")
            unita = mil.SupportoLogistico(nome, soldati, intervento)
            controllo.registra_unita(unita)

        case "5":
            nome = input("Nome unità: ")
            soldati = int(input("Numero soldati: "))
            area = input("Area da esplorare: ")
            unita = mil.Ricognizione(nome, soldati, area)
            controllo.registra_unita(unita)

        # Mostra unità
        case "6":
            controllo.mostra_unita()

        # Dettagli + azione speciale
        case "7":
            nome = input("Inserisci il nome dell'unità: ")
            unita = controllo.unita_registrate.get(nome)

            if unita is None:
                print("Unità non trovata.")
            else:
                controllo.dettagli_unita(nome)

                print("\nVuoi eseguire l'azione speciale? (s/n)")
                if input("> ").lower() == "s":
                    if isinstance(unita, mil.Fanteria):
                        unita.costruisci_trincea()
                    elif isinstance(unita, mil.Artiglieria):
                        unita.calibra_artiglieria()
                    elif isinstance(unita, mil.Cavalleria):
                        unita.esplora_terreno()
                    elif isinstance(unita, mil.SupportoLogistico):
                        unita.rifornisci_unita()
                    elif isinstance(unita, mil.Ricognizione):
                        unita.conduci_ricognizione()

        # Uscita
        case "0":
            print("Chiusura programma.")
            break
        
        # Input non valido
        case _:
            print("Scelta non valida, riprova.")