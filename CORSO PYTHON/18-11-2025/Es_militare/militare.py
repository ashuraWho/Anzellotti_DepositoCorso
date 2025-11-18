# --------------------------------------------------------------
# --------------------- MODULO: MILITARE -----------------------
# --------------------------------------------------------------

# --------------------------------------------------------------
# 1) CLASSE BASE: UNITA' MILITARE
# --------------------------------------------------------------

class UnitaMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati
    
    def muovi(self):
        print(f"L'unità '{self.nome}' con {self.numero_soldati} soldati si sta muovendo.")
    
    def attacca(self):
        print(f"L'unità '{self.nome}' con {self.numero_soldati} soldati è all'attacco!")
    
    def ritira(self):
        print(f"L'unità '{self.nome}' con {self.numero_soldati} soldati si sta ritirando strategicamente.")

# --------------------------------------------------------------
# 2) CLASSI SPECIALIZZATE
# Ogni classe rappresenta un tipo di unità con un compito diverso.
# --------------------------------------------------------------

class Fanteria(UnitaMilitare):
    def __init__(self, nome, numero_soldati, numero_trincee):
        super().__init__(nome, numero_soldati) # Richiamo il costruttore della classe base.
        self.numero_trincee = numero_trincee # Variabile specifica della fanteria.
    
    def costruisci_trincea(self):
        print(f"La fanteria '{self.nome}' costruisce {self.numero_trincee} trincee temporanee.")

class Artiglieria(UnitaMilitare):
    def __init__(self, nome, numero_soldati, numero_pezzi):
        super().__init__(nome, numero_soldati)
        self.numero_pezzi = numero_pezzi
    
    def calibra_artiglieria(self):
        print(f"L'artiglieria '{self.nome}' calibra {self.numero_pezzi} pezzi per ottenere massima precisione.")

class Cavalleria(UnitaMilitare):
    def __init__(self, nome, numero_soldati, quadrante):
        super().__init__(nome, numero_soldati)
        self.quadrante = quadrante
    
    def esplora_terreno(self):
        print(f"La cavalleria '{self.nome}' esplora il quadrante {self.quadrante}.")

class SupportoLogistico(UnitaMilitare):
    def __init__(self, nome, numero_soldati, tipo_intervento):
        super().__init__(nome, numero_soldati)
        self.tipo_intervento = tipo_intervento # Il tipo spiega se l'unità fa rifornimento o manutenzione.
    
    def rifornisci_unita(self):
        print(f"Il supporto '{self.nome}' effettua {self.tipo_intervento} per {self.numero_soldati} soldati.")

class Ricognizione(UnitaMilitare):
    def __init__(self, nome, numero_soldati, area):
        super().__init__(nome, numero_soldati)
        self.area = area
    
    def conduci_ricognizione(self):
        print(f"La ricognizione '{self.nome}' conduce una missione di sorveglianza in '{self.area}'.")

# --------------------------------------------------------------
# 3) CLASSE DI CONTROLLO
# Questa classe eredita da tutte le altre e gestisce un registro
# con tutte le unità create.
# --------------------------------------------------------------

class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione):
    def __init__(self):
        UnitaMilitare.__init__(self, "Comando Centrale", 0) # Non rappresenta una vera unità -> inizializzato a 0
        self.unita_registrate = {} # Dizionario che conserva tutte le unità aggiunte.
    
    def registra_unita(self, unita):
        self.unita_registrate[unita.nome] = unita # Inserisco l'unità nel dizionario usando il suo nome.
        print(f"Unità '{unita.nome}' registrata con successo.")
    
    def _recupera_tipo_base(self, unita):
        # Funzione di utilità per restituire un nome semplice della classe
        # isinstance() -> verifica se un oggetto appartiene a una certa classe o a una sua sottoclasse -> True/False
        if isinstance(unita, Fanteria):
            return "Fanteria"
        if isinstance(unita, Artiglieria):
            return "Artiglieria"
        if isinstance(unita, Cavalleria):
            return "Cavalleria"
        if isinstance(unita, SupportoLogistico):
            return "Supporto Logistico"
        if isinstance(unita, Ricognizione):
            return "Ricognizione"
        return "Unità"
    
    def mostra_unita(self):
        # Stampo tutte le unità caricate.
        if not self.unita_registrate:
            print("Non sono ancora state registrate unità.")
            return
        
        print("\n--- Elenco unità registrate ---")
        for nome, unita in self.unita_registrate.items():
            tipo = self._recupera_tipo_base(unita)
            print(f"- {nome} | Tipo: {tipo} | Soldati: {unita.numero_soldati}")
    
    def dettagli_unita(self, nome):
        unita = self.unita_registrate.get(nome) # Recupero l'unità dal dizionario.
        if unita is None:
            print(f"L'unità '{nome}' non esiste nel registro.")
            return
        
        print(f"\nDettagli per l'unità '{nome}':")
        tipo = self._recupera_tipo_base(unita)
        print(f"Tipo: {tipo}")
        print(f"Numero soldati: {unita.numero_soldati}")
        
        # Indico all'utente quale metodo speciale può chiamare.
        if isinstance(unita, Fanteria):
            print("Azione speciale disponibile: costruisci trincea")
        elif isinstance(unita, Artiglieria):
            print("Azione speciale disponibile: calibra artiglieria")
        elif isinstance(unita, Cavalleria):
            print("Azione speciale disponibile: esplora terreno")
        elif isinstance(unita, SupportoLogistico):
            print("Azione speciale disponibile: rifornisci unita")
        elif isinstance(unita, Ricognizione):
            print("Azione speciale disponibile: conduci ricognizione")