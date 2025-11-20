# CLASSE BASE
class MetodoPagamento:
    def effettua_pagamento(self, importo):
        print("Metodo base: pagamento generico.")


# CLASSI DERIVATE
class CartaDiCredito(MetodoPagamento):
    def __init__(self, pin):
        self.pin = pin

    def effettua_pagamento(self, importo):
        pin_prova = input("Inserisci PIN: ")
        
        if pin_prova == self.pin:
            print(f"Pagamento con Carta effettuato! Importo: {importo}€")
        else:
            print("Pagamento negato: PIN errato.")


class PayPal(MetodoPagamento):
    def __init__(self, email):
        self.email = email

    def effettua_pagamento(self, importo):
        email_prova = input("Inserisci email PayPal destinatario: ")
        
        if email_prova == self.email:
            print(f"Pagamento con PayPal effettuato! Importo: {importo}€")
        else:
            print("Pagamento negato: email errata.")


class BonificoBancario(MetodoPagamento):
    def __init__(self, iban):
        self.iban = iban

    def effettua_pagamento(self, importo):
        iban_prova = input("Inserisci IBAN destinatario: ")
        
        if iban_prova == self.iban:
            print(f"Pagamento con Bonifico effettuato! Importo: {importo}€")
        else:
            print("Pagamento negato: IBAN errato.")


# -------------------------------------------------------------------------
# GESTORE PAGAMENTI
class GestorePagamenti:
    def __init__(self, metodo: MetodoPagamento):
        self.metodo = metodo

    def paga(self, importo):
        self.metodo.effettua_pagamento(importo)
