# --------------------------------------------------------------
# ---------------------- ESERCITAZIONE DEF ---------------------
# --------------------------------------------------------------

import random # Importazione del modulo random

# --------------------------------------------------------------
# --------------------------------------------------------------

# Funzione per il gioco "Indovina il Numero"
def indovina_numero():
    numero = random.randint(1, 100)
    tentativi = 0
    indovinato = False

    print("\nBenvenuto al gioco 'Indovina il Numero'!")
    print("Ho scelto un numero tra 1 e 100. Riuscirai a indovinarlo?")

    while not indovinato:
        prova = int(input("Inserisci il tuo tentativo (numero intero): "))
        tentativi += 1
        
        while prova < 1 or prova > 100:
            prova = int(input("Hai perso un tentativo! Inserisci un numero intero TRA 1 e 100: "))
            tentativi += 1

        if prova < numero:
            print("Troppo basso! Riprova.")
        elif prova > numero:
            print("Troppo alto! Riprova.")
        else:
            indovinato = True
            print(f"Congratulazioni! Hai indovinato il numero {numero} in {tentativi} tentativi.")

# --------------------------------------------------------------

# Funzione per generare la sequenza di Fibonacci fino a n
def Fibonacci(n):
    a, b = 0, 1 # Inizializzazione dei primi due numeri della sequenza
    sequenza = [] # Lista per memorizzare la sequenza di Fibonacci
    
    while a <= n:
        sequenza.append(a)
        a, b = b, a + b # Aggiornamento dei valori di a e b
    return sequenza

# --------------------------------------------------------------
# --------------------------------------------------------------

opzione = False

while not opzione:
    comando = input("\nScegli l'opzione: exit, base, avanzato. ")

    match comando:
        case "exit":  # --- exit ---
            print("\nUscita dal programma.")
            opzione = True
            
        case "base":  # --- base ---
            print("\nAvvio dell'esercitazione base: indovina il numero...")
            
            riprova = True
            
            while riprova:
                indovina_numero() # Chiamata della funzione per giocare
                
                risposta = input("\nVuoi giocare di nuovo? (si per continuare): ").lower()
                if risposta != 'si':
                    riprova = False
                    print("\nGrazie per aver giocato. Chiusura del gioco.")
                
                
        case "avanzato":  # --- avanzato ---
            print("\nAvvio dell'esercitazione avanzata: sequenza di Fibonacci fino a N...")
            
            numeri = [] # Lista per memorizzare i numeri N inseriti
            numeri_fib = [] # Lista per memorizzare le sequenze di Fibonacci generate
            record = [numeri, numeri_fib] # Lista di liste
            
            riprova = True
            
            while riprova:
                n = int(input("\nInserisci un numero intero positivo N per generare la sequenza di Fibonacci fino a N: "))
                while n <= 0:
                    n = int(input("Inserisci un numero POSITIVO: "))
                
                numeri.append(n)
                
                fib = Fibonacci(n) # Chiamata della funzione Fibonacci
                numeri_fib.append(fib)
                
                print(f"\nLa sequenza di Fibonacci fino a {n} è:")
                print(fib) # Stampa della sequenza di Fibonacci
                
                risposta = input("\nVuoi riprovare? (si per continuare): ").lower()
                if risposta != 'si':
                    riprova = False
                    print("\nChiusura del programma Fibonacci.")
                    
                    print("\nRiepilogo delle sequenze di Fibonacci generate:")
                    nomi = ["N", "Sequenza"] # Nomi delle liste
                    
                    for i in range(len(record)): # Primo ciclo sulle liste
                        print(f"\n{nomi[i]}:")  # Stampa il nome
                        
                        for valore in record[i]: # Secondo ciclo dentro la sottolista
                            print(valore)
            
        case _:
            print("\nComando non riconosciuto.")
            print("Per favore, inserisci 'exit' o 'start'.")