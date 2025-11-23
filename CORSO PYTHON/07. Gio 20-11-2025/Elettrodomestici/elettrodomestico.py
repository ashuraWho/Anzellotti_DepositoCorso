# CLASSE BASE
class Elettrodomestico:
    ANNO_CORRENTE = 2025
    
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str):
        self.__marca = marca
        self.__modello = modello
        self.__anno_acquisto = anno_acquisto
        self.__guasto = guasto
        self.__costo_base_diagnosi = 50 # Euro
        
    # Metodi Getter
    def get_marca(self):
        return self.__marca # Stringa

    def get_modello(self):
        return self.__modello # Stringa

    def get_anno_acquisto(self):
        return self.__anno_acquisto # Intero

    def get_guasto(self):
        return self.__guasto # Stringa
    
    # Metodi Setter
    def set_marca(self, nuova__marca):
        self.__marca = nuova__marca
    
    def set_modello(self, nuovo__modello):
        self.__modello = nuovo__modello
    
    def set_anno_acquisto(self, nuovo__anno_acquisto: int):
            
        if 0 < nuovo__anno_acquisto <= self.ANNO_CORRENTE:
            self.__anno_acquisto = nuovo__anno_acquisto
            return True
        
        return False
        
    def set_guasto(self, nuovo__guasto: str):
        self.__guasto = nuovo__guasto
        
    # Metodo Descrittivo
    def descrizione(self):
        return f"Elettrodomestico: {self.__marca} - {self.__modello}. Acquistato nel {self.__anno_acquisto}. Guasto: {self.__guasto}."

    # Metodo per il costo base (polimorfico)
    def stima_costo_base(self):
        return self.__costo_base_diagnosi