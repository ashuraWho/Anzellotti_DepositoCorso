import modulo as mod

def main():
    
    pagamenti_utente = {}   # dizionario
    
    while True:
        nome = input("\nInserisci il tuo nome: ")
        if nome not in pagamenti_utente: # Aggiunta al dizionario
            pagamenti_utente[nome] = []
        
        print("\nScegli metodo pagamento:")
        print("(1) Carta di Credito")
        print("(2) PayPal")
        print("(3) Bonifico Bancario")
        print("(0) Esci")

        scelta = input("\nScelta: ")

        match scelta:
            case "1":
                importo = float(input("\nImporto da pagare: "))
                pin = input("\nImposta il PIN della carta: ")
                metodo = mod.CartaDiCredito(pin=pin)
                m = "Carta di Credito"

            case "2":
                importo = float(input("\nImporto da pagare: "))
                email = input("\nInserisci l'email del tuo conto PayPal: ")
                metodo = mod.PayPal(email=email)
                m = "PayPal"

            case "3":
                importo = float(input("\nImporto da pagare: "))
                iban = input("\nInserisci l'IBAN destinatario: ")
                metodo = mod.BonificoBancario(iban=iban)
                m = "Bonifico Bancario"
                
            case "0":
                print("\nUscita.")
                break

            case _:
                print("\nScelta non valida.")
                continue
        
        # POLIMORFISMO
        gestore = mod.GestorePagamenti(metodo) # Prendo il metodo scelto nel match
        gestore.paga(importo)

        pagamenti_utente[nome].append(m)

        print(f"Metodo '{m}' salvato per l'utente {nome}.\n")

    print("\nStorico pagamenti utenti:")
    for nome, m in pagamenti_utente.items():
        print(f"- {nome}: {m}")

if __name__ == "__main__":
    main()