import flotta as fl
import veicolo as vt

""" Non faccio match e gestione input per mancanza di tempo (così ripassso un pochino) """

def main():
    
    flotta = fl.GestoreFlotta()
    
    # Camion: 5 assi, Max 10000 kg
    camion1 = vt.Camion("AX123YZ", 10000, 5) 
    flotta.aggiungi_veicolo(camion1) 
    
    # Furgone: Max 1500 kg, Elettrico
    furgone1 = vt.Furgone("FR456GH", 1500, "elettrico")
    flotta.aggiungi_veicolo(furgone1)

    # Motocarro: Max 500 kg, 3 anni di servizio
    motocarro1 = vt.Motocarro("MO789LK", 500, 3)
    flotta.aggiungi_veicolo(motocarro1)
    
    print("\n--- DEMO OPERAZIONI DI CARICO E SCARICO ---")
    
    # Tentativo di carico del Camion -> OK
    camion1.carica(6000)
    # Tentativo di sovraccarico del Camion -> NO 
    camion1.carica(5000) 
    # Scarico
    camion1.scarica()
    
    # Carico del Furgone
    furgone1.carica(500)

    flotta.stampa_veicoli()
    
    # Calcolo costo totale di manutenzione
    costo_totale = flotta.costo_totale_manutenzione()
    print(f"\nCosto Totale Manutenzione della Flotta: {costo_totale:.2f} €")
    
    # 5. Rimuovi un veicolo
    flotta.rimuovi_veicolo("FR456GH")
    
    # Report finale
    flotta.stampa_veicoli()


if __name__ == "__main__":
    main()