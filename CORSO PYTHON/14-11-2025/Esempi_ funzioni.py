# --------------------------------------------------------------
# --------------------------- FUNZIONI -------------------------
# --------------------------------------------------------------

#Questa funzione saluta la persona il cui nome viene passato come argomento.
def saluta(nome):
    print(f"Ciao, {nome}!")
    print("Benvenuto al corso di Python.")
    
saluta("Luca") # Chiamata della funzione con l'argomento "Luca"


# Questa funzione calcola la somma di due numeri e restituisce il risultato.
def somma(a, b):
    return a + b

risultato = somma(5, 3) # Chiamata della funzione con gli argomenti 5 e 3
print(f"La somma è: {risultato}") # Stampa il risultato della somma