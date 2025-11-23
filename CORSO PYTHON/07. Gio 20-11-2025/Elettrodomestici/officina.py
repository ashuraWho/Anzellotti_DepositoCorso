from elettrodomestico import Elettrodomestico
from lavatrice import Lavatrice
from frigorifero import Frigorifero
from forno import Forno
from riparazione import TicketRiparazione

# Classe che gestisce l'elenco degli elettrodomestici e dei ticket
class Officina:
    
    def __init__(self, nome: str):
        self._nome = nome
        self._elettrodomestici: list[Elettrodomestico] = []
        self._tickets: list[TicketRiparazione] = []
        
    def aggiungi_elettrodomestico(self, ed: Elettrodomestico):
        self._elettrodomestici.append(ed)
        print(f"\nAggiunto: {ed.get_marca()} - {ed.get_modello()}")

    def aggiungi_ticket(self, ticket: TicketRiparazione):
        self._tickets.append(ticket)
        print(f"\nTicket {ticket.get_id()} creato per {ticket.get_elettrodomestico().get_marca()}")

    def chiudi_ticket(self, id_ticket: str):
        for ticket in self._tickets:
            if ticket.get_id() == id_ticket:
                ticket.aggiorna_stato("CHIUSO")
                print(f"\nTicket {id_ticket} CHIUSO.")
                return
        print(f"\nErrore: Ticket {id_ticket} non trovato.")

    def stampa_tickets_aperti(self):
        print(f"\n--- TICKETS APERTI/IN LAVORAZIONE ({self._nome}) ---")
        trovati = False
        for ticket in self._tickets:
            if ticket.get_stato() != "CHIUSO":
                print(ticket)
                print("\n---------------------------------")
                trovati = True
        if not trovati:
            print("\nNessun ticket aperto o in lavorazione.")

    def totale_preventivi(self): # Restituisce la somma dei preventivi di tutti i ticket attivi
        return sum(ticket.calcola_preventivo() for ticket in self._tickets if ticket.get_stato() != "CHIUSO")

    def statistiche_per_tipo(self): # Conta quanti elettrodomestici ci sono in riparazione per tipo
        print("\n--- STATISTICHE PER TIPO DI RIPARAZIONE ---")
        
        n_lavatrici = 0
        n_frigoriferi = 0
        n_forni = 0
        n_altro = 0
        
        for ticket in self._tickets:
            ed = ticket.get_elettrodomestico()
            
            if isinstance(ed, Lavatrice):
                n_lavatrici += 1
            elif isinstance(ed, Frigorifero):
                n_frigoriferi += 1
            elif isinstance(ed, Forno):
                n_forni += 1
            else:
                n_altro += 1

        print(f"Numero di Lavatrici in riparazione: {n_lavatrici}")
        print(f"Numero di Frigoriferi in riparazione: {n_frigoriferi}")
        print(f"Numero di Forni in riparazione: {n_forni}")
        print(f"Numero di altri ED in riparazione: {n_altro}")
        
        # Stampa i costi totali per tipo
        costo_lavatrici = sum(t.calcola_preventivo() for t in self._tickets if isinstance(t.get_elettrodomestico(), Lavatrice))
        costo_frigoriferi = sum(t.calcola_preventivo() for t in self._tickets if isinstance(t.get_elettrodomestico(), Frigorifero))
        costo_forni = sum(t.calcola_preventivo() for t in self._tickets if isinstance(t.get_elettrodomestico(), Forno))

        print(f"\nCosto totale preventivi Lavatrici: {costo_lavatrici:.2f} €")
        print(f"Costo totale preventivi Frigoriferi: {costo_frigoriferi:.2f} €")
        print(f"Costo totale preventivi Forni: {costo_forni:.2f} €")