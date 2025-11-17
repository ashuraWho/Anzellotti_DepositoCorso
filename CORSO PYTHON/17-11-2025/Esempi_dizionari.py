# --------------------------------------------------------------
# -------------------------- DIZIONARI -------------------------
# --------------------------------------------------------------

# I dizionari sono una struttura dati che consente di memorizzare coppie di chiavi e valori. 
# -> sono rappresentati dal tipo di dato dict e sono racchiusi tra parentesi graffe { }

# Puoi creare un dizionario assegnando un insieme di coppie chiave-valore a una variabile. 
# Le coppie chiave-valore sono separate da due punti : e le coppie sono separate da virgole.

studente = {
    
    "nome" : "Emanuele",
    "età" : 24,
    "sesso" : "maschio"
}

# Puoi accedere ai valori di un dizionario utilizzando le chiavi corrispondenti.
print(studente["nome"]) # Output: "Emanuele"

# Puoi modificare il valore associato a una chiave di un dizionario assegnando un nuovo valore a quella chiave.
studente["età"] = 25
print(studente) # Output: {'nome': Emanuele', 'età': 25, 'sesso' : 'maschio'}

# ---------------------------------------------

# METODI:
# - keys() per ottenere una lista di tutte le chiavi
# - values() per ottenere una lista di tutti i valori
# - items() per ottenere una lista di tutte le coppie chiave-valore
# - get() per ottenere il valore associato a una chiave (senza generare un errore se la chiave non esiste)

print(studente.keys()) # Output: dict_keys(['nome', 'età', 'sesso'])
print(studente.values()) # Output: dict_values([Emanuele', 25, 'maschio'])

# ---------------------------------------------

# Andiamo a creare 3 input che riempiamo con booleano un numero intero e una stringa  
# li inseriamo in una lista e inseriamo la lista come valore di un dizionario per chiave ‘tipididato’

booleano = input("Inserisci un booleano (true/false): ").lower() == "true"
intero = int(input("Inserisci un numero intero: "))
stringa = input("Inserisci una stringa: ")

dati2 = {
    
    "numero" : intero,
    "booleano" : booleano,
    "stringa" : stringa
    
}

lista = [dati2]

dati = {
    
    "tipididato": [booleano, intero, stringa],
    "dizionari" : lista
}

print(dati)

for x,y in dati2.items():
    
    print("chiave ", x)
    print("valore ", y)