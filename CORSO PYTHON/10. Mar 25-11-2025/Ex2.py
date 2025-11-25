import numpy as np

def salva_su_file(nome_file, contenuto, sovrascrivi):
    
    """
        - Se sovrascrivi = True -> 'w'
        - Se sovrascrivi = False -> 'a'  
    """
    
    mode = "w" if sovrascrivi else "a"
    with open(nome_file, mode) as f:
        f.write(contenuto)


def esecuzione():

    arr_lin = np.linspace(0, 10, 50) # Creo array con linspace

    arr_rand = np.random.random(50) # Creo array con random

    arr_sum = arr_lin + arr_rand # Sommo gli elementi

    somma_totale = np.sum(arr_sum) # Sommo i due array

    somma_maggiori_5 = np.sum(arr_sum[arr_sum > 5]) # Sommo elementi > 5

    # Stampa su schermo
    print("\n--- RISULTATI ---")
    print("Array linspace:\n", arr_lin)
    print("\nArray random:\n", arr_rand)
    print("\nArray somma:\n", arr_sum)
    print("\nSomma totale:", somma_totale)
    print("Somma > 5:", somma_maggiori_5)

    # Stampa su file
    testo = (
        "\n--- Nuova esecuzione ---\n"
        f"Array linspace:\n{arr_lin}\n\n"
        f"Array random:\n{arr_rand}\n\n"
        f"Array somma:\n{arr_sum}\n\n"
        f"Somma totale: {somma_totale}\n"
        f"Somma > 5: {somma_maggiori_5}\n"
    )

    return testo


def main():
    nome_file = "ex2_risultati.txt"

    while True:
        print("\n--- Gestione file ---")
        print("(1) Sovrascrivi il file")
        print("(2) Aggiungi al file")
        print("(0) Esci")

        scelta = input("\nScegli (0-2): ")
    
        match scelta:
            case "1":
                sovrascrivi = True
            case "2":
                sovrascrivi = False
            case "0":
                    print("\nFine programma.")
                    break
            case _:
                print("\nScelta non valida, imposto 'sovrascrivi = False'.")
                sovrascrivi = False

        while True:
            contenuto = esecuzione() # Prendo il 'testo'
            salva_su_file(nome_file, contenuto, sovrascrivi)

            print(f"\nDati salvati su '{nome_file}'.")

            print("\n--- Menu ---")
            print("(1) Ripeti")
            print("(2) Torna al menu principale")

            azione = input("\nScegli 1 o 2: ")

            match azione:
                case "1":
                    continue
                case "2":
                    print("\nTorna al menu principale.")
                    break
                case _:
                    print("\nScelta non valida, termino il programma.")
                    break


if __name__ == "__main__":
    main()