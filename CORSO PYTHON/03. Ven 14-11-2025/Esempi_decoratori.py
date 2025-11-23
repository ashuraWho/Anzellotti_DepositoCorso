# --------------------------------------------------------------
# -------------------------- DECORATORI ------------------------
# --------------------------------------------------------------

def decoratore(funzione): # Definizione del decoratore
    def wrapper(): # Funzione wrapper che avvolge la funzione originale
        print(f"\nPrima di eseguire la funzione.") # Azione prima della funzione
        funzione() # Chiamata della funzione originale
        print(f"\nDopo aver eseguito la funzione.") # Azione dopo la funzione
    return wrapper

@decoratore # Applicazione del decoratore alla funzione saluta
def saluta(): # Funzione da decorare
    print("Ciao! Questa è una funzione decorata.") # Corpo della funzione
    
saluta() # Chiamata della funzione decorata

# --------------------------------------------------------------

def decoratore_con_argomenti(funzione): # Definizione del decoratore con argomenti
    def wrapper(*args, **kwargs): # Funzione wrapper che accetta argomenti
        print(f"\nPrima di eseguire la funzione con argomenti: {args}, {kwargs}") # Azione prima della funzione
        risultato = funzione(*args, **kwargs) # Chiamata della funzione originale con argomenti
        print(f"\nDopo aver eseguito la funzione con argomenti.") # Azione dopo la funzione
        return risultato # Restituzione del risultato della funzione originale
    return wrapper

@decoratore_con_argomenti # Applicazione del decoratore con argomenti
def somma(a, b): # Funzione da decorare che somma due numeri
    return a + b # Restituzione della somma

print(f"\nIl risultato della somma è: {somma(5, 7)}") # Stampa del risultato