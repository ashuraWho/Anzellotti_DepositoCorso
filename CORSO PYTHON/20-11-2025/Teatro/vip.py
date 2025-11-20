from posto import Posto

# CLASSI DERIVATE DA 'Posto'
class PostoVIP(Posto):
    def __init__(self, numero, fila, servizi_extra = None):
        super().__init__(numero, fila)
        self.servizi_extra = servizi_extra if servizi_extra else [] # Lista di stringhe es. ["Accesso al lounge", "Servizio in posto"]

    def prenota(self):
        if super().prenota():
            print("\nServizi extra attivati:")
            for servizio in self.servizi_extra:
                print(f"- {servizio}")
            return True
        return False

    def __str__(self):
        stato = "Occupato" if self._occupato else "Libero"
        servizi = ", ".join(self.servizi_extra) if self.servizi_extra else "Nessuno"
        return f"Posto VIP {self._fila}{self._numero} - {stato} - Servizi: {servizi}"

class PostoStandard(Posto):
    def __init__(self, numero, fila, costo=0.0):
        super().__init__(numero, fila)
        self.costo = costo

    def prenota(self):
        print(f"Costo: {self.costo} €")
        return super().prenota()

    def __str__(self):
        stato = "Occupato" if self._occupato else "Libero"
        return f"Posto Standard {self._fila}{self._numero} - {stato} - {self.costo} €"