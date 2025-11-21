# Lettura
file = open("CORSO PYTHON/21-11-2025/IO/nome_file.txt", "r") # Ho messo il path relativo
contenuto = file.read() # Legge l'intero contenuto del file 
riga = file.readline() # Legge una singola riga del file
file.close()

# Scrittura
file = open("CORSO PYTHON/21-11-2025/IO/nome_file.txt", "w") # Ho messo il path relativo
contenuto = file.write("Esempio di scrittura sul file.") # Sovrascrive il file
file.close()

# Il file viene chiuso automaticamente al termine del blocco 'with'
with open("CORSO PYTHON/21-11-2025/IO/nome_file.txt", "r") as file:
    contenuto = file.read()