from posto import Posto

# CLASSE TEATRO
class Teatro:
    def __init__(self):
        self._posti = []

    def aggiungi_posto(self, posto):
        # Controllo se il posto esiste già
        for p in self._posti:
            if p.get_numero() == posto.get_numero() and p.get_fila() == posto.get_fila():
                print(f"Posto {posto.get_fila()}{posto.get_numero()} già esistente")
                return
        self._posti.append(posto)
        print(f"Aggiunto: {posto}")

    def prenota_posto(self, numero, fila):
        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                return posto.prenota()
        print(f"Posto {fila}{numero} non trovato")
        return False
    
    def libera_posto(self, numero, fila):
        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                return posto.libera()
        print(f"Posto {fila}{numero} non trovato")
        return False

    def stampa_posti_occupati(self):
        print("Posti occupati:")
        for posto in self._posti:
            if posto.is_occupato():
                print(f"- {posto}")

    def stampa_tutti_posti(self):
        print("Tutti i posti:")
        for posto in self._posti:
            print(f"- {posto}")