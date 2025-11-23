# SISTEMA ASTRATTO DI TRASPORTO MERCI

from abc import ABC, abstractmethod

# CLASSE ASTRATTA
class VeicoloTrasporto(ABC):
    def __init__(self, targa: str, peso_massimo: int):
        self._targa = targa
        self._peso_massimo = peso_massimo # in kg
        self._carico_attuale = 0 # Inizializzato a 0 kg
        
    """ --- Metto prima i metodi astratti e poi quelli concreti --- """
    
    # Metodo astratto: deve essere implementato dalle sottoclassi
    @abstractmethod
    def costo_manutenzione(self): # Calcola il costo di manutenzione secondo regole diverse
        pass
    
    # Metodi concreti
    def carica(self, peso: int): # Aumenta il carico attuale se possibile, altrimenti segnala
        nuovo_carico = self._carico_attuale + peso
        
        if nuovo_carico <= self._peso_massimo:
            self._carico_attuale = nuovo_carico
            print(f"\nCarico di {peso} kg aggiunto a targa {self._targa}. Carico attuale: {self._carico_attuale} kg.")
            return True
        else:
            eccesso = nuovo_carico - self._peso_massimo
            print(f"\nERRORE: Il peso di {peso} kg supera la capacità massima di {self._peso_massimo} kg. Eccesso: {eccesso} kg.")
            return False
        
    def scarica(self): # Riporta il carico attuale a 0
        self._carico_attuale = 0
        print(f"\nTarga {self._targa} scaricata. Carico attuale: 0 kg.")
        
    # Metodo per la descrizione (lo metto in visione della funzione nella classe GestoreFlotta)
    def descrizione_veicolo(self):
        return (f"Targa: {self._targa} | Capacità Max: {self._peso_massimo} kg | Carico Attuale: {self._carico_attuale} kg")

# ------------------------------------------------------

# SOTTOCLASSI CONCRETE
class Camion(VeicoloTrasporto):
    
    def __init__(self, targa: str, peso_massimo: int, numero_assi: int):
        super().__init__(targa, peso_massimo)
        self._numero_assi = numero_assi

    # Implementazione del metodo astratto
    def costo_manutenzione(self): # 100€ per asse + 1€ per kg di carico massimo

        costo_assi = 100.0 * self._numero_assi
        costo_peso = 1.0 * self._peso_massimo
        
        return costo_assi + costo_peso
    
class Furgone(VeicoloTrasporto):
    
    def __init__(self, targa: str, peso_massimo: int, alimentazione: str):
        super().__init__(targa, peso_massimo)
        self._alimentazione = alimentazione.lower()

    # Implementazione del metodo astratto
    def costo_manutenzione(self): # 200€ se elettrico, 150€ se diesel e metto 175€ per altro

        if self._alimentazione == "elettrico":
            return 200.0
        elif self._alimentazione == "diesel":
            return 150.0
        else:
            return 175.0 # Costo default per altro

class Motocarro(VeicoloTrasporto):
    
    def __init__(self, targa: str, peso_massimo: int, anni_servizio: int):
        super().__init__(targa, peso_massimo)
        self._anni_servizio = anni_servizio

    # Implementazione del metodo astratto
    def costo_manutenzione(self): # 50€ per ogni anno di servizio
        return 50.0 * self._anni_servizio