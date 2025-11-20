from elettrodomestico import Elettrodomestico

class Frigorifero(Elettrodomestico): # Sottoclasse
    
    # Valori di maggiorazione definiti internamente
    LITRI_LIMITE = 300 # Litri
    MAGGIORAZIONE_FREEZER_GRANDE = 1.5 # +50%
    MAGGIORAZIONE_SOLO_FREEZER = 1.2 # +20%
    
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str, litri: int, ha_freezer: bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        
        self._litri = litri
        self._ha_freezer = ha_freezer

    # Sovrascrittura del metodo stima_costo_base
    def stima_costo_base(self):
        base = super().stima_costo_base()
        
        if self._ha_freezer and self._litri > self.LITRI_LIMITE:
            return base * self.MAGGIORAZIONE_FREEZER_GRANDE  # Maggiorazione
        
        elif self._ha_freezer:
             return base * self.MAGGIORAZIONE_SOLO_FREEZER
         
        return base