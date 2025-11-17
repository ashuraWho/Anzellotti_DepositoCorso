import time

def calcola_tempo(funzione):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        risultato = funzione(*args, **kwargs)
        end_time = time.time()
        print(f"Tempo di esecuzione: {end_time - start_time} secondi")
        return risultato
    return wrapper

@calcola_tempo
def calcolo_lento():
    time.sleep(2)
    print("Calcolo completato")

# Chiamata alla funzione decorata
calcolo_lento()