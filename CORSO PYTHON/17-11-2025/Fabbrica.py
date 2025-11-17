# --------------------------------------------------------------
# ------------------- ESERCITAZIONE FABBRICA -------------------
# --------------------------------------------------------------

# ====================================================================================
# Come EXTRA ho aggiunto uno storico che tiene traccia dei movimenti nell'inventario
# ====================================================================================

class Prodotto: # Classe prodotto base
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome # Nome del prodotto
        self.costo_produzione = costo_produzione # Costo per produrre il prodotto
        self.prezzo_vendita = prezzo_vendita # Prezzo del prodotto per il pubblico

    def calcola_profitto(self): # Profitto (unitario) = prezzo vendita - costo produzione
        return self.prezzo_vendita - self.costo_produzione
    

# CLASSI PARALLELE
class Elettronica:
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia_anni):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.garanzia_anni = garanzia_anni
    
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

class Abbigliamento:
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.materiale = materiale
    
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

# ------------------------------------------------

class Fabbrica: # Classe fabbrica
    def __init__(self):
        self.inventario = {} # Tengo traccia di ogni prodotto in magazzino
        # Dizionario inventario = {nome_prodotto: {"prodotto": istanza, "quantita": n}}
        
        self.storico = [] # Lista che registra tutte le operazioni effettuate
        # Lista di operazioni: {"tipo": "aggiunta/vendita/reso", "prodotto": nome, "quantita": n, "profitto": x}

    def aggiungi_prodotto(self, prodotto, quantita): # Aggiungo prodotti all'inventario
        if prodotto.nome in self.inventario: # Se il prodotto è nell'inventario
            self.inventario[prodotto.nome]["quantita"] += quantita
        else:
            self.inventario[prodotto.nome] = {"prodotto": prodotto, "quantita": quantita}
        
        # Registro l'operazione nello storico
        self.storico.append({
            
            "tipo": "aggiunta",
            "prodotto": prodotto.nome,
            "quantita": quantita
            
        })
            
        print(f"\nAggiunti {quantita} pezzi di {prodotto.nome} nell'inventario.")

    def vendi_prodotto(self, nome_prodotto, quantita):
        if nome_prodotto not in self.inventario:
            print(f"\n{nome_prodotto} non è presente nell'inventario.")
            return
        
        item = self.inventario[nome_prodotto] # Prendo in considerazione l'oggetto da vendere
        if item["quantita"] < quantita:
            print(f"\nQuantità insufficiente per {nome_prodotto}. Disponibili: {item['quantita']}")
            return
        
        item["quantita"] -= quantita
        profitto_totale = item["prodotto"].calcola_profitto() * quantita
        
        # Registro l'operazione nello storico
        self.storico.append({
            
            "tipo": "vendita",
            "prodotto": nome_prodotto,
            "quantita": quantita,
            "profitto": profitto_totale
            
        })
        
        print(f"\nVenduti {quantita} pezzi di {nome_prodotto}. Profitto: {profitto_totale:.2f}€")

    def resi_prodotto(self, nome_prodotto, quantita):
        if nome_prodotto not in self.inventario:
            print(f"\n{nome_prodotto} non è presente nell'inventario, creo la voce e aggiungo il reso.")
            return
        
        self.inventario[nome_prodotto]["quantita"] += quantita
        
        # Registro l'operazione nello storico
        self.storico.append({
            
            "tipo": "reso",
            "prodotto": nome_prodotto,
            "quantita": quantita
            
        })
        
        print(f"\nRicevuti {quantita} pezzi di {nome_prodotto} come reso.")
    
    def stampa_inventario(self):
        if not self.inventario:
            print("\nInventario vuoto.")
            return
        
        print("\nInventario:")
        for nome, entry in self.inventario.items():
            print(f" - {nome}: {entry['quantita']} pezzi")
    
    def stampa_storico(self):
        if not self.storico:
            print("\nStorico operazioni vuoto.")
            return
        
        print("\n--- Storico Operazioni ---")
        for i, operazione in enumerate(self.storico, 1):
            tipo = operazione["tipo"]
            prodotto = operazione["prodotto"]
            quantita = operazione["quantita"]
            
            if tipo == "vendita":
                profitto = operazione.get("profitto", 0)
                print(f"{i}. VENDITA: {quantita} pezzi di {prodotto} - Profitto: {profitto:.2f}€")
                
            elif tipo == "aggiunta":
                print(f"{i}. AGGIUNTA: {quantita} pezzi di {prodotto}")
                
            elif tipo == "reso":
                print(f"{i}. RESO: {quantita} pezzi di {prodotto}")

# ------------------------------------------------

def input_prodotto(): # Funzione che mi fa inserire un prodotto nuovo
    while True:
        tipo = input("Tipo prodotto (elettronica/abbigliamento): ").strip().lower()
        nome = input("Nome prodotto: ")
        costo = float(input("Costo produzione: "))
        prezzo = float(input("Prezzo vendita: "))

        match tipo:
            
            case "elettronica":
                garanzia = int(input("Garanzia (anni): "))
                return Elettronica(nome, costo, prezzo, garanzia)
            
            case "abbigliamento":
                materiale = input("Materiale: ")
                return Abbigliamento(nome, costo, prezzo, materiale)
            
            case _:
                print("Tipo non valido, riprova.")
                
# -----------------------------------------------------------------------------------

fabbrica = Fabbrica()

while True:
    print("\n--- Menu ---")
    print("(1) Aggiungi prodotto")
    print("(2) Vendi prodotto")
    print("(3) Registra reso")
    print("(4) Mostra inventario")
    print("(5) Mostra storico operazioni")
    print("(6) Esci")

    scelta = input("Seleziona un'opzione (1-6): ")

    match scelta:
        
        case "1":
            prodotto = input_prodotto()
            quantita = int(input("Quantità da aggiungere: "))
            fabbrica.aggiungi_prodotto(prodotto, quantita)
            
        case "2":
            nome = input("Nome prodotto da vendere: ")
            quantita = int(input("Quantità da vendere: "))
            fabbrica.vendi_prodotto(nome, quantita)
            
        case "3":
            nome = input("Nome prodotto da restituire: ")
            quantita = int(input("Quantità restituite: "))
            fabbrica.resi_prodotto(nome, quantita)
            
        case "4":
            fabbrica.stampa_inventario()
            
        case "5":
            fabbrica.stampa_storico()
            
        case "6":
            print("Chiusura gestione fabbrica.")
            break
        
        case _:
            print("Scelta non valida, riprova.")