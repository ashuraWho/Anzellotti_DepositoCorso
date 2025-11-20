from elettrodomestico import Elettrodomestico
from lavatrice import Lavatrice
from frigorifero import Frigorifero
from forno import Forno
from riparazione import TicketRiparazione
from officina import Officina

def crea_elettrodomestico_da_input():
    print("\n--- CREAZIONE NUOVO ELETTRODOMESTICO ---")
    
    # Dati comuni
    marca = input("Marca: ")
    modello = input("Modello: ")
    
    # Gestione robusta dell'input per l'anno (usa la costante definita nella classe)
    ANNO_CORRENTE = Elettrodomestico.ANNO_CORRENTE 
    while True:
        try:
            anno = int(input(f"\nAnno di acquisto (max {ANNO_CORRENTE}): "))
            if 0 < anno <= ANNO_CORRENTE: 
                break
            else:
                print(f"L'anno deve essere un numero intero positivo e non può essere nel futuro (max {ANNO_CORRENTE}).")
        except ValueError:
            print("Input non valido. Inserisci un numero intero per l'anno.")
            
    guasto = input("Descrizione del guasto: ")
    
    # Scelta del tipo:
    print("\nTipo di Elettrodomestico:")
    print("(1) Lavatrice")
    print("(2) Frigorifero")
    print("(3) Forno")
    tipo_scelto = input("\nScegli il tipo (1-3): ")

    match tipo_scelto:
        case "1":
            while True:
                try:
                    capacita = int(input("\nCapacità in kg: "))
                    giri = int(input("Giri centrifuga (RPM): "))
                    return Lavatrice(marca, modello, anno, guasto, capacita, giri)
                except ValueError:
                    print("Input non valido. Inserisci numeri interi.")
        
        case "2":
            while True:
                try:
                    litri = int(input("\nCapacità in litri: "))
                    ha_freezer = input("Ha il freezer? (S/N): ").upper()
                    return Frigorifero(marca, modello, anno, guasto, litri, ha_freezer)
                except ValueError:
                    print("Input non valido. Inserisci un numero intero per i litri.")
            
        case "3":
            tipo_al = input("\nTipo di alimentazione (elettrico/gas): ")
            ha_ventilato = input("È ventilato? (S/N): ").upper()
            return Forno(marca, modello, anno, guasto, tipo_al, ha_ventilato)
            
        case _:
            print("\nTipo non valido. Ritorno al menu principale.")
            return None

def aggiungi_nuovo_ticket_interattivo(officina: Officina):
    nuovo_ed = crea_elettrodomestico_da_input()
    
    if nuovo_ed:
        # Generazione ID ticket progressivo
        id_ticket = f"T-{len(officina._tickets) + 1:03d}" 
        
        nuovo_ticket = TicketRiparazione(id_ticket, nuovo_ed)
        
        costo_aggiuntivo_input = input("\nInserisci un costo aggiuntivo iniziale per ricambi/manodopera (0 se nessuno): ")
        try:
            costo_aggiuntivo = float(costo_aggiuntivo_input)
            nuovo_ticket.aggiungi_costo(costo_aggiuntivo)
        except ValueError:
            print("Costo aggiuntivo non valido, impostato a 0.")

        nota = input("Aggiungi una nota iniziale (lascia vuoto se non necessaria): ")
        if nota:
            nuovo_ticket.aggiungi_nota(nota)
            
        officina.aggiungi_ticket(nuovo_ticket)
        print(f"\nNUOVO TICKET CREATO:")
        print(nuovo_ticket)


def inizializza_dati_di_esempio(officina: Officina):
    print("\n--- Inizializzazione Dati di Esempio ---")
    
    # Lavatrice (stima costo base: 50.0 * 1.3 = 65.0)
    lavatrice1 = Lavatrice("Indesit", "IWDE7145B", 2018, "Cestello bloccato", 9, 1400)
    ticket1 = TicketRiparazione("T-001", lavatrice1)
    ticket1.aggiungi_costo(45.50) 
    ticket1.aggiungi_nota("Ordinato ricambio cestello.")
    officina.aggiungi_ticket(ticket1)
    
    # Frigorifero (stima costo base: 50.0 * 1.5 = 75.0)
    frigo1 = Frigorifero("Samsung", "RB37J5000SA", 2020, "Non raffredda", 350, True)
    ticket2 = TicketRiparazione("T-002", frigo1)
    ticket2.aggiungi_costo(120.00)
    officina.aggiungi_ticket(ticket2)
    
    # Forno (stima costo base: 50.0 + 20.0 + 10.0 = 80.0)
    forno1 = Forno("Whirlpool", "AKZM8480NB", 2022, "Resistenza bruciata", "gas", True)
    ticket3 = TicketRiparazione("T-003", forno1)
    ticket3.aggiorna_stato("IN LAVORAZIONE")
    officina.aggiungi_ticket(ticket3)
    
    print("Dati di esempio caricati. Pronti per l'interazione.")