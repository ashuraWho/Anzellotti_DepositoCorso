# CLASSE BASE
class Posto:
    def __init__(self, numero: int, fila: str):
        self._numero = numero
        self._fila = fila
        self._occupato = False
    
    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"\nPosto {self._fila}{self._numero} prenotato correttamente.")
            return True
        else:
            print(f"\nIl posto {self._fila}{self._numero} è già prenotato.")
            return False
    
    def libera(self):
        if self._occupato:
            self._occupato = False
            print(f"\nPosto {self._fila}{self._numero} liberato.")
            return True
        else:
            print(f"\nIl posto {self._fila}{self._numero} non era prenotato.")
            return False
        
    # Getter
    def get_numero(self):
        return self._numero

    def get_fila(self):
        return self._fila

    def is_occupato(self):
        return self._occupato

    def __str__(self):
        stato = "Occupato" if self._occupato else "Libero"
        return f"Posto {self._fila}{self._numero} - {stato}"