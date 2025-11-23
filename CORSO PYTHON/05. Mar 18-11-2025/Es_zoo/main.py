# --------------------------------------------------------------
# -------------------------- MAIN: ZOO -------------------------
# --------------------------------------------------------------

import zoo

while True:
    print("\n--- Scegli un animale ---")
    print("(1) Animale generico")
    print("(2) Cane")
    print("(3) Gatto")
    print("(4) Formica")
    print("(5) Esci")

    scelta = input("\nSeleziona un'opzione (1-5): ")

    match scelta:
        
        case "1":
            nome = input("\nNome animale: ")
            eta = int(input("Età animale: "))
            
            animale_generico = zoo.Animale(nome, eta)
            animale_generico.fai_suono()
            
        case "2":
            nome = input("\nNome cane: ")
            eta = int(input("Età cane: "))
            
            while True:
                comportamento = input("\nE' addestrato? (s/n) ")
                if comportamento == "s":
                    cane = zoo.Cane(nome, eta, True)
                    cane.addestramento()
                    break

                elif comportamento == "n":
                    cane = zoo.Cane(nome, eta, False)
                    break
                
                else:
                    print("\nScelta non valida, riprova.")
                    continue
                
        case "3":
            nome = input("\nNome gatto: ")
            eta = int(input("Età gatto: "))
            dorme = int(input("Quante ore dorme al giorno? "))
            
            gatto = zoo.Gatto(nome, eta, dorme)
            gatto.riposino()
            
        case "4":
            nome = input("\nNome formica: ")
            eta = int(input("Età formica: "))
            ruolo = input("\nChe ruolo ha all'interno del formicaio? ")
            
            formica = zoo.Formica(nome, eta, ruolo)
            formica.lavoro()
            
        case "5":
            print("\nChiusura programma.")
            break
        
        case _:
            print("\nScelta non valida, riprova.")