import veicolo as vt

# Gestisce l'inventario di tutti i veicoli della flotta
class GestoreFlotta:
    
    def __init__(self):
        self._lista_veicoli: list[vt.VeicoloTrasporto] = [] # Lista di oggetti derivati da VeicoloTrasporto

    def aggiungi_veicolo(self, veicolo: vt.VeicoloTrasporto):
        self._lista_veicoli.append(veicolo)
        print(f"\nVeicolo {veicolo._targa} aggiunto alla flotta.")

    def rimuovi_veicolo(self, targa: str):
        veicolo_da_rimuovere = None
        
        for veicolo in self._lista_veicoli:
            if veicolo._targa == targa:
                veicolo_da_rimuovere = veicolo
                break
        
        if veicolo_da_rimuovere:
            self._lista_veicoli.remove(veicolo_da_rimuovere)
            print(f"Veicolo targa {targa} rimosso dalla flotta.")
        else:
            print(f"ERRORE: Targa {targa} non trovata.")

    def costo_totale_manutenzione(self): # Polimorfismo sugli oggetti astratti
        costo_totale = 0.0
        
        for veicolo in self._lista_veicoli:
            costo_totale += veicolo.costo_manutenzione()
            
        return costo_totale

    def stampa_veicoli(self):
        print("\n--- Report Flotta Attuale ---")
        if not self._lista_veicoli:
            print("Flotta vuota.")
            return
        
        for veicolo in self._lista_veicoli:
            print(f"- {veicolo.descrizione_veicolo()} | Manutenzione Stimata: {veicolo.costo_manutenzione():.2f} €")