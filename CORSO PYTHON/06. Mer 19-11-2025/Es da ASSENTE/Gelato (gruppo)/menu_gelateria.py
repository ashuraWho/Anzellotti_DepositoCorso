import gusto

class MenuGelateria: # Gestisce l'elenco dei gusti disponibili
    def __init__(self):
        self.gusti = []  # lista di oggetti Gusto, Premium o Vegano

    def aggiungi_gusto(self, gusto):
        self.gusti.append(gusto)

    def rimuovi_gusto(self, nome):
        nome = nome.lower()
        trovato = False

        for g in self.gusti:
            if g.get_nome().lower() == nome:
                self.gusti.remove(g)
                trovato = True
                print(f"Gusto '{g.get_nome()}' rimosso.\n")
                break

        if not trovato:
            print(f"Il gusto '{nome}' non è presente nel menu.\n")

    def lista_gusti(self):
        print("\n--- MENU GELATERIA ---")
        
        for g in self.gusti:
            if isinstance(g, gusto.GustoPremium):
                print(g.descrizione_premium())
                
            elif isinstance(g, gusto.GustoVegano):
                print(g.descrizione_vegano())
                
            else:
                print(g.descrizione())
                