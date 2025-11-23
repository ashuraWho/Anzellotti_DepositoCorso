from elettrodomestico import Elettrodomestico

class Lavatrice(Elettrodomestico): # Sottoclasse
    
    # Valori di maggiorazione definiti internamente
    CAPACITA_LIMITE = 8 # kg
    MAGGIORAZIONE_PERCENTUALE = 1.3 # +30%
    
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str, capacita_kg: int, giri_centrifuga: int):
        super().__init__(marca, modello, anno_acquisto, guasto)
        
        self._capacita_kg = capacita_kg
        self._giri_centrifuga = giri_centrifuga

    # Sovrascrittura del metodo stima_costo_base
    def stima_costo_base(self):
        base = super().stima_costo_base()
        
        if self._capacita_kg > self.CAPACITA_LIMITE: # Il costo base è maggiorato se la capacità è elevata
            return base * self.MAGGIORAZIONE_PERCENTUALE  # Maggiorazione
        
        return base