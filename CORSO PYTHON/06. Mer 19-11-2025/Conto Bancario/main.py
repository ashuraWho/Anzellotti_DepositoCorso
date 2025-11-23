import conto_bancario as cb

# Creo un conto con titolare e saldo iniziale
c = cb.ContoBancario("Mario Rossi", 100)

while True:
    print("\n--- MENU CONTO BANCARIO ---")
    print("(1) Visualizza titolare")
    print("(2) Cambia titolare")
    print("(3) Visualizza saldo")
    print("(4) Deposita")
    print("(5) Preleva")
    print("(0) Esci")

    scelta = input("\nScegli un'opzione (0-5): ")

    match scelta:
        case "1":
            print("\nTitolare:", c.get_titolare())

        case "2":
            nuovo = input("\nInserisci nuovo titolare: ")
            c.set_titolare(nuovo)
            importo = float(input("\nInserisci importo da depositare: "))
            c.deposita(importo)
            print("\nTitolare aggiornato con successo.")

        case "3":
            print("\nSaldo:", c.visualizza_saldo())

        case "4":
            importo = float(input("\nInserisci importo da depositare: "))
            c.deposita(importo)

        case "5":
            importo = float(input("\nInserisci importo da prelevare: "))
            c.preleva(importo)

        case "0":
            print("Uscita dal programma.")
            break

        case _:
            print("Scelta non valida. Riprova.")