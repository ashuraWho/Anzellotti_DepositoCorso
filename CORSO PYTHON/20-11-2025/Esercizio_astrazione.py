from abc import ABC, abstractmethod

# 1. CLASSE ASTRATTA: Impiegato (classe base)
class Impiegato(ABC): # Non può essere istanziata direttamente

    def __init__(self, nome: str, cognome: str, stipendio_base: float):
        self._nome = nome
        self._cognome = cognome
        self._stipendio_base = stipendio_base
    
    def __str__(self):
        return f"Nome: {self._nome} {self._cognome}, Ruolo: {self.__class__.__name__}, Stipendio Base: {self._stipendio_base:.2f} €"

    # Metodo Astratto: deve essere implementato da ogni classe derivata
    @abstractmethod
    def calcola_stipendio(self): # Metodo astratto per il calcolo dello stipendio mensile
        pass

# CLASSI DERIVATE
class ImpiegatoFisso(Impiegato):

    def __init__(self, nome: str, cognome: str, stipendio_base: float):
        super().__init__(nome, cognome, stipendio_base)

    # Implementazione del metodo astratto
    def calcola_stipendio(self): # Lo stipendio è semplicemente lo stipendio base
        return self._stipendio_base

class ImpiegatoAProvvigione(Impiegato): # Riceve lo stipendio base + bonus basato sulle vendite

    def __init__(self, nome: str, cognome: str, stipendio_base: float, vendite_del_mese: float, percentuale_provvigione: float):
        super().__init__(nome, cognome, stipendio_base)
        self._vendite_del_mese = vendite_del_mese
        self._percentuale_provvigione = percentuale_provvigione

    # Implementazione del metodo astratto
    def calcola_stipendio(self): # Calcola lo stipendio come stipendio base + (vendite * percentuale)
        bonus_provvigione = self._vendite_del_mese * self._percentuale_provvigione
        stipendio_totale = self._stipendio_base + bonus_provvigione
        
        return stipendio_totale

# ----------------------------------------------------------------------

def stampa_informazioni_impiegati(lista_impiegati: list[Impiegato]):

    print("--- Report Stipendi Mensili ---")
    
    for impiegato in lista_impiegati:
        stipendio_calcolato = impiegato.calcola_stipendio()
        
        print(f"\n**Impiegato:** {impiegato._nome} {impiegato._cognome}")
        print(impiegato)
        print(f"**Stipendio Netto Totale:** {stipendio_calcolato:.2f} €")
        
        # Se è un impiegato a provvigione, mostra il dettaglio
        if isinstance(impiegato, ImpiegatoAProvvigione):
            provvigione = stipendio_calcolato - impiegato._stipendio_base
            print(f"   -> Bonus Provvigione: {provvigione:.2f} €")

def main():
    
    # 1. Creazione degli oggetti Impiegato
    
    # Impiegato Fisso
    filippo = ImpiegatoFisso("Filippo", "Rossi", 2500.00)
    
    # Impiegato a Provvigione (Vendite: 20000€, Provvigione: 5%)
    alessandra = ImpiegatoAProvvigione("Alessandra", "Verdi", 1800.00, 20000.00, 0.05)
    
    # Altro Impiegato a Provvigione (Vendite: 5000€, Provvigione: 10%)
    giovanni = ImpiegatoAProvvigione("Giovanni", "Neri", 1500.00, 5000.00, 0.10)
    
    # 2. Creazione della lista
    lista_ufficio = [filippo, alessandra, giovanni]
    
    # 3. Stampa e calcolo
    stampa_informazioni_impiegati(lista_ufficio)

if __name__ == "__main__":
    main()