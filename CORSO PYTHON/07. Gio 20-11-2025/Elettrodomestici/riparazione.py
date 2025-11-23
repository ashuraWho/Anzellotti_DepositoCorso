from elettrodomestico import Elettrodomestico

# Ticket aperto in officina
class TicketRiparazione:
    
    STATI = ["APERTO", "IN LAVORAZIONE", "CHIUSO"] # "costanti"

    def __init__(self, id_ticket: str, elettrodomestico: Elettrodomestico, stato: str = "APERTO"):
        self._id_ticket = id_ticket
        self._elettrodomestico = elettrodomestico
        self._stato = stato.upper() if stato.upper() in self.STATI else "APERTO"
        self._note = []
        self._costo_aggiuntivo = 0.0 # Costo per ricambi, manodopera, ecc.

    # Metodi Getter
    def get_id(self):
        return self._id_ticket # Stringa

    def get_elettrodomestico(self):
        return self._elettrodomestico # Elettrodomestico
    
    def get_stato(self):
        return self._stato # Stringa
    
    def get_costo_aggiuntivo(self):
        return self._costo_aggiuntivo # Float

    # Metodi Setter/Utilità
    def aggiorna_stato(self, nuovo_stato: str):
        nuovo_stato = nuovo_stato.upper()
        
        if nuovo_stato in self.STATI:
            self._stato = nuovo_stato
        else:
            print(f"\nERRORE: Stato '{nuovo_stato}' non valido.")
            
    def aggiungi_nota(self, nota: str):
        self._note.append(nota)
        
    def aggiungi_costo(self, costo: float):
        self._costo_aggiuntivo += costo

    # Metodo per il calcolo del preventivo
    def calcola_preventivo(self, *voci_extra: float):
        
        """
            Calcola il costo totale. Utilizza stima_costo_base() dell'elettrodomestico 
            specifico e aggiunge voci extra e costi aggiuntivi.
        """
        
        costo_base = self._elettrodomestico.stima_costo_base()
        
        # Somma tutte le voci extra passate come parametri variabili
        costo_extra_voci = sum(voci_extra)
        
        costo_totale = costo_base + self._costo_aggiuntivo + costo_extra_voci
        
        return costo_totale

    def __str__(self):
        return (f"\n--- Ticket ID: {self._id_ticket} ---\n"
                f"Stato: {self._stato}\n"
                f"Elettrodomestico: {self._elettrodomestico.descrizione()}\n"
                f"Costo Base Stima: {self._elettrodomestico.stima_costo_base():.2f} €\n"
                f"Costo Aggiuntivo: {self._costo_aggiuntivo:.2f} €\n"
                f"Preventivo Attuale: {self.calcola_preventivo():.2f} €\n"
                f"Note: {self._note}")