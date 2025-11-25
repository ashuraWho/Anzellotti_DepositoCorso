# Semplicememnte mi salva sul file (nome file in input)

def salvaFile(testo, filename):
    with open(filename, "a") as f:
        f.write(testo + "\n\n")
    print(f"Risultato salvato su {filename}\n")