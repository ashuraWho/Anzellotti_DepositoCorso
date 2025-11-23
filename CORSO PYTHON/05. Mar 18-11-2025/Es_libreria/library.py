# --------------------------------------------------------------
# --------------------- MODULO: LIBRERIA -----------------------
# --------------------------------------------------------------

# Classe 'Libro'
class Libro:
    
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
    
    # --- Metodi ---
    def descrizione(self):
        return f"Libro: '{self.titolo}', '{self.autore}', ISBN {self.isbn}"
     
# Classe 'Libreria'
class Libreria:
    
    def __init__(self):
        self.catalogo = [] # Lista con oggetti della classe 'Libro'
     
    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)
        
    def rimuovi_libro(self, isbn): # Rimuove il libro con quell'ISBN
        for libro in self.catalogo:
            if libro.isbn == isbn:
                self.catalogo.remove(libro)
                print(f"\nLibro con ISBN {isbn} rimosso.")
                return
            
        print(f"\nNessun libro con ISBN {isbn} trovato.")

    def cerca_per_titolo(self, titolo): # Restituisce una lista di libri con quel titolo
        lista_libri = []
        
        for libro in self.catalogo:
            if libro.titolo == titolo:
                lista_libri.append(libro)
        
        return lista_libri
        
    def mostra_catalogo(self):
        if not self.catalogo: # Se non ci sono libri nel catalogo
            print("\nIl catalogo è vuoto.")
        else:
            print("\nCatalogo libri:")
            for libro in self.catalogo:
                print(f"- {libro.descrizione()}") # Stampo la descrizione di tutti i libri nel catalogo