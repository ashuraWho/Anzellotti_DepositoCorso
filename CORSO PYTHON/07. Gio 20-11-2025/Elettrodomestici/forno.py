from elettrodomestico import Elettrodomestico

class Forno(Elettrodomestico): # Sottoclasse

    # Valori di maggiorazione definiti internamente
    INCREMENTO_GAS = 1.3 # +30%
    INCREMENTO_VENTILATO = 1.5 # +50%
    
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str, tipo_alimentazione: str, ha_ventilato: bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        
        self._tipo_alimentazione = tipo_alimentazione.lower()
        self._ha_ventilato = ha_ventilato

    # Sovrascrittura del metodo stima_costo_base
    def stima_costo_base(self):
        base = super().stima_costo_base()
        
        if self._tipo_alimentazione == "gas":
            return base * self.INCREMENTO_GAS # Costo maggiore per il gas
            
        if self._ha_ventilato:
            return base * self.INCREMENTO_VENTILATO # Costo maggiore per la funzione ventilata
            
        return base