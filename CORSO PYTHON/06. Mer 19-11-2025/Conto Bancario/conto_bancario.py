class ContoBancario:
    def __init__(self, titolare, saldo_iniziale=0.0):
        
        """
        Attributi privati
            __titolare: contiene il nome del titolare del conto
            __saldo: contiene il saldo attuale del conto
         """
         
        self.__titolare = None
        self.__saldo = 0.0

        # Inizializzo titolare e saldo
        self.set_titolare(titolare)
        self.__saldo = saldo_iniziale

    def get_titolare(self): # Permette di leggere il nome del titolare
        return self.__titolare
    
    def set_titolare(self, nuovo_titolare):
        if not isinstance(nuovo_titolare, str) or nuovo_titolare.strip() == "":
            print("\nIl titolare deve essere una stringa non vuota.") # Errore in caso di valore errato
        else:
            self.__titolare = nuovo_titolare.strip() # Se valido, aggiorna l'attributo privato

    def visualizza_saldo(self): # Non permette modifiche esterne al saldo (solo lettura)
        return self.__saldo

    def deposita(self, importo):
        if importo <= 0:
            print("\nL'importo deve essere positivo.") # Importi negativi o nulli non sono validi
        else:
            self.__saldo += importo
            print(f"Hai depositato {importo:.2f}€. Saldo: {self.__saldo:.2f}€")

    def preleva(self, importo):
        if importo <= 0:
            print("\nL'importo deve essere positivo.")
        elif importo > self.__saldo:
            print("\nFondi insufficienti.")
        else:
            self.__saldo -= importo
            print(f"Hai prelevato {importo:.2f}€. Saldo: {self.__saldo:.2f}€")