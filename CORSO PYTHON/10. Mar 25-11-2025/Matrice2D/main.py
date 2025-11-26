import matrice2D as m2D

def main():
    nome_file = input("\nInserisci il nome del file dove salvare i risultati: ")

    matrice = None

    while True:
        print("\n--- MENU ---")
        print("(1) Crea matrice 2D (random)")
        print("(2) Sotto-matrice centrale")
        print("(3) Trasposta")
        print("(4) Somma elementi")
        print("(5) Moltiplicazione element-wise")
        print("(6) Media elementi")
        print("(7) Determinante")
        print("(0) Uscire")

        scelta = input("\nScelta: ")

        match scelta:
            
            case "1":
                matrice = m2D.crea_matrice(nome_file)

            case "2":
                if matrice is not None:
                    matrice = m2D.sotto_matrice_centrale(matrice, nome_file)
                else:
                    print("\nCrea prima una matrice!")

            case "3":
                if matrice is not None:
                    matrice = m2D.trasposta(matrice, nome_file)
                else:
                    print("\nCrea prima una matrice!")

            case "4":
                if matrice is not None:
                    m2D.somma(matrice, nome_file)
                else:
                    print("\nCrea prima una matrice!")

            case "5":
                if matrice is not None:
                    m2D.elementwise(matrice, nome_file)
                else:
                    print("\nCrea prima una matrice!")

            case "6":
                if matrice is not None:
                    m2D.media(matrice, nome_file)
                else:
                    print("\nCrea prima una matrice!")

            case "7":
                if matrice is not None:
                    m2D.determinante(matrice, nome_file)
                else:
                    print("\nCrea prima una matrice!")
                    
            case "0":
                print("\nUscita")
                break

            case _:
                print("\nScelta non valida.")


if __name__ == "__main__":
    main()
