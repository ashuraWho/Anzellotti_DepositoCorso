# --------------------------------------------------------------
# ------------------------ ESERCITAZIONE -----------------------
# --------------------------------------------------------------

# Creo classe 'Ristorante':
# Args: self, nome (nome del ristorante), tipo_cucina (tipo di cucina offerta)
class Ristorante:
    
    def __init__(self, nome, tipo_cucina, menu = None):
        # self è l'istanza corrente
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False # Attributo della classe: se il ristorante è aperto
        self.menu = menu or {} # Se ho o non ho il menu

    def descrivi_ristorante(self):
        print(f"\nIl ristorante '{self.nome}' offre cucina {self.tipo_cucina}.") # Accedo agli attributi dell'istanza tramite self

    def stato_apertura(self):
        stato = "aperto" if self.aperto else "chiuso"
        print(f"\nIl ristorante è attualmente {stato}.")

    def apri_ristorante(self):
        self.aperto = True
        print(f"\n{self.nome} è ora aperto!")

    def chiudi_ristorante(self):
        self.aperto = False
        print(f"\n{self.nome} è ora chiuso.")

    def aggiungi_al_menu(self, piatto, prezzo):
        self.menu[piatto] = prezzo # Uso self.menu per aggiornare il menu dell'istanza
        print(f"\nAggiunto '{piatto}' al menu a {prezzo:.2f}€.")

    def togli_dal_menu(self, piatto):
        if piatto in self.menu:
            del self.menu[piatto]
            print(f"\nRimosso '{piatto}' dal menu.")
        else:
            print(f"\n'{piatto}' non è presente nel menu.")

    def stampa_menu(self):
        if not self.menu:
            print("\nIl menu è vuoto.")
            return
        print("\nMenu:")
        for piatto, prezzo in self.menu.items():
            print(f" - {piatto}: {prezzo:.2f}€")
            
            
# --- Raccolta di input dall’utente ---
nome_input = input("\nNome del ristorante: ")
tipo_input = input("Tipo di cucina offerta: ")

# Costruisco il menu dinamicamente
menu_input = {}
numero_piatti = int(input("\nQuanti piatti vuoi inserire nel menu iniziale? "))
for _ in range(numero_piatti):
    piatto = input("\nNome del piatto: ")
    prezzo = float(input("Prezzo del piatto: "))
    menu_input[piatto] = prezzo

# Creo l’istanza usando gli input
ristorante = Ristorante(nome_input, tipo_input, menu_input)

# Test di tutti i metodi
ristorante.descrivi_ristorante()
ristorante.stato_apertura()
ristorante.apri_ristorante()
ristorante.stato_apertura()
ristorante.stampa_menu()

# Modifica menu
nuovo_piatto = input("\nAggiungi un nuovo piatto: ")
nuovo_prezzo = float(input("Prezzo del nuovo piatto: "))
ristorante.aggiungi_al_menu(nuovo_piatto, nuovo_prezzo)
ristorante.stampa_menu()

piatto_da_togliere = input("\nQuale piatto vuoi togliere? ")
ristorante.togli_dal_menu(piatto_da_togliere)
ristorante.stampa_menu()

ristorante.chiudi_ristorante()
ristorante.stato_apertura()