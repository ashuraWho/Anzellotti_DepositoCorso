from elettrodomestico import Elettrodomestico
from lavatrice import Lavatrice
from frigorifero import Frigorifero
from forno import Forno
from riparazione import TicketRiparazione
from officina import Officina
import inserimento

def main():
    
    # 1. Inizializzazione dell'Officina
    officina = Officina("Riparazioni ElettroTech")
    print(f"\n--- Benvenuto nell'Officina {officina._nome} ---")
    
    # Carica dati di esempio (opzionale)
    inserimento.inizializza_dati_di_esempio(officina)

    # 3. Interfaccia utente
    while True:
        print("\n---------------------------------")
        print("Seleziona un'operazione:")
        print("(1) Stampa Tickets Aperti")
        print("(2) Chiudi Ticket")
        print("(3) Statistiche per Tipo")
        print("(4) Totale Preventivi Attivi")
        print("(5) Aggiungi nuovo ticket")
        print("(0) Esci")
        
        scelta = input("\nScelta (0-5): ")
        
        match scelta:
            case "1":
                officina.stampa_tickets_aperti()
            
            case "2":
                id_da_chiudere = input("\nInserisci l'ID del Ticket da chiudere (es. T-001): ")
                officina.chiudi_ticket(id_da_chiudere)
                
            case "3":
                officina.statistiche_per_tipo()
                
            case "4":
                totale = officina.totale_preventivi()
                print(f"\nTotale Preventivi Attivi: {totale:.2f} €")
            
            case "5":
                totale = officina.totale_preventivi()
                inserimento.aggiungi_nuovo_ticket_interattivo(officina)
                
            case "0":
                print("\nArrivederci!")
                break
                
            case _:
                print("\nScelta non valida. Riprova.")

if __name__ == "__main__":
    main()