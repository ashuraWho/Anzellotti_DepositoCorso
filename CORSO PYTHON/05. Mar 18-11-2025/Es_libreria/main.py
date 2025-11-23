# --------------------------------------------------------------
# ---------------------- MAIN: LIBRERIA ------------------------
# --------------------------------------------------------------

import library as lib

# Creo libri
libro1 = lib.Libro("Guida Galattica per gli Autostoppisti", "Douglas Adams", "123")
libro2 = lib.Libro("Il Gioco del Trono", "George R. R. Martin", "456")
libro3 = lib.Libro("Il Signore degli Anelli", "J.R.R. Tolkien", "789")

libreria = lib.Libreria() # Creo libreria

# Aggiungo i libri al catalogo
libreria.aggiungi_libro(libro1)
libreria.aggiungi_libro(libro2)
libreria.aggiungi_libro(libro3)

libreria.mostra_catalogo() # Mostro il catalogo

# Cerco per titolo
print("\nRicerca per titolo 'Guida Galattica per gli Autostoppisti':")
risultati = libreria.cerca_per_titolo("Guida Galattica per gli Autostoppisti")
for libro in risultati:
    print("- ", libro.descrizione())

libreria.rimuovi_libro("123") # Rimuovo 'Guida Galattica per gli Autostoppisti' per ISBN

# Catalogo finale
print("\nCatalogo post-rimozione:")
libreria.mostra_catalogo()