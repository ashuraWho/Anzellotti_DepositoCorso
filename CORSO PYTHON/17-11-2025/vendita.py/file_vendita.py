# --------------------------------------------------------------
# ------------ FILE: ANALIZZATORE DI DATI DI VENDITA -----------
# --------------------------------------------------------------

import modulo_vendita as mv

while True:
    
    importo = input("\nInserisci gli importi di vendita separati da spazio: ")
    
    if importo.strip() == "": # Se l'utente non inserisce niente
        print("Non sono stati inseriti dati. Riprova.")
        continue

    dati = importo.split()
    vendite = [] # Dati di vendita -> ogni numero è l'importo totale di vendite in un dato giorno

    try: # Esegui questo blocco di codice
        for i in dati:
            numero = int(i)
            vendite.append(numero)
        break # Se tutto va bene si esce dal while
    
    except ValueError: # Se trovi questo errore allora stampa errore
        print("\nErrore: hai inserito un valore non numerico.")
        print("Riprova inserendo solo NUMERI interi separati da spazi.")
        

analizzatore = mv.Analizzatore(vendite) # Creo l'oggetto analizzatore a cui passo 'vendite'
    
totale = analizzatore.totale() # Calcolo il totale
media = analizzatore.media() # Calcolo la media
over_media = analizzatore.sopra_media() # Vendite sopra la media

print("\n--- Risultati ---")
print("- Dati di vendita inseriti: ", vendite)
print("- Vendite totali: ", totale)
print("- Media vendite: ", media)
    
print("\n--- Giorni con vendite sopra la media ---")
if len(over_media) == 0:
    print("Non ci sono giorni con vendite sopra la media :(")
else:
    for giorno, valore in over_media:
        print(f"- Giorno {giorno}: vendita = {valore}")