# --------------------------------------------------------------
# ------------------ ESERCITAZIONE RISTORANTE ------------------
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
            
# -----------------------------------------------------------------------------------

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

# Modifica menu
while True:
    print("\nScegli una delle opzioni: ")
    print("(1) Vedere la descrizione del ristorate")
    print("(2) Vedere il menu")
    print("(3) Cambiare il menu")
    print("(4) Vedere lo stato del ristorante (aperto/chiuso)")
    print("(5) Aprire il ristorante")
    print("(6) Chiudere il ristorante")
    print("(7) Exit")
    
    comando = int(input("\nScegli una delle opzioni (1-6): "))

    match comando:
        
        case 1:
            ristorante.descrivi_ristorante()
        
        case 2:
            ristorante.stampa_menu()
            
        case 3:
            scelta = True
            
            while scelta:

                modifica = input("\nVuoi aggiungere, eliminare un piatto o uscire? (add/del) ")
                if modifica == "add":
                    nuovo_piatto = input("\nAggiungi un nuovo piatto: ")
                    nuovo_prezzo = float(input("Prezzo del nuovo piatto: "))
                    ristorante.aggiungi_al_menu(nuovo_piatto, nuovo_prezzo)
                    ristorante.stampa_menu()
                elif modifica == "del":
                    piatto_da_togliere = input("\nQuale piatto vuoi togliere? ")
                    ristorante.togli_dal_menu(piatto_da_togliere)
                    ristorante.stampa_menu()
                else:
                    print("\nInserire 'add' o 'del'.")
                
                ripetere = input("\nVuoi cambiare altro? (s/n) ")
                if modifica == "s":
                    continue
                elif modifica == "n":
                    scelta = False
                else:
                    print("\nInserire 's' o 'n'.")
                          
        case 4:
            ristorante.stato_apertura()
            
        case 5:
            ristorante.apri_ristorante()
            
        case 6:
            ristorante.chiudi_ristorante()
            
        case 7:
            print("\nUscita.")
            break
            
        case _:
            print("\nComando non riconosciuto.")
            print("Per favore, inserisci 's' o 'n'.")
       
