class Biblioteca:
    def __init__(self):
        self.libri = []

    def crea_libro(self, titolo, autore, pagine):
        self.libri.append((titolo, autore, pagine))

    def stampa_libri(self):
        for titolo, autore, pagine in self.libri:
            print(titolo, ";", autore, ";", pagine, "pagine")

biblioteca = Biblioteca()

while True:
    titolo = input("\nTitolo (invio per terminare): ")
    if titolo == "":
        break
    autore = input("Autore: ")
    pagine = input("Numero pagine: ")
    biblioteca.crea_libro(titolo, autore, pagine)

print("Catalogo:")
biblioteca.stampa_libri()