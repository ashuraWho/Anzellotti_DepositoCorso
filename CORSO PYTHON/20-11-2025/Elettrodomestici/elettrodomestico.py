# CLASSE BASE
class Elettrodomestico:
    ANNO_CORRENTE = 2025
    
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str):
        self._marca = marca
        self._modello = modello
        self._anno_acquisto = anno_acquisto
        self._guasto = guasto
        self._costo_base_diagnosi = 50 # Euro
        
    # Metodi Getter
    def get_marca(self):
        return self._marca # Stringa

    def get_modello(self):
        return self._modello # Stringa

    def get_anno_acquisto(self):
        return self._anno_acquisto # Intero

    def get_guasto(self):
        return self._guasto # Stringa
    
    # Metodi Setter
    def set_marca(self, nuova_marca):
        self._marca = nuova_marca
    
    def set_modello(self, nuovo_modello):
        self._modello = nuovo_modello
    
    def set_anno_acquisto(self, nuovo_anno_acquisto: int):
            
        if 0 < nuovo_anno_acquisto <= self.ANNO_CORRENTE:
            self._anno_acquisto = nuovo_anno_acquisto
            return True
        
        return False
        
    def set_guasto(self, nuovo_guasto: str):
        self._guasto = nuovo_guasto
        
    # Metodo Descrittivo
    def descrizione(self):
        return f"Elettrodomestico: {self._marca} - {self._modello}. Acquistato nel {self._anno_acquisto}. Guasto: {self._guasto}."

    # Metodo per il costo base (polimorfico)
    def stima_costo_base(self):
        return self._costo_base_diagnosi