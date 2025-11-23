import menu_gelateria as mg
import gusto

def main():
    menu = mg.MenuGelateria()

    # GUSTI DEFAULT
    # Gusto base -> nome: str, prezzo_base: float, allergeni: list
    g1 = gusto.Gusto("Cioccolato", 2.0, ["latte"])
    g2 = gusto.Gusto("Fragola", 2.0, ["nessuno"])
    g3 = gusto.Gusto("Pistacchio", 2.5, ["frutta secca"])

    # Gusto premium -> nome: str, prezzo_base: float, allergeni: list, ingredienti_speciali: list, sovrapprezzo: float
    p1 = gusto.GustoPremium("Nocciola Suprema", 2.5, ["frutta secca"], ["panna montata"], 0.5)
    p2 = gusto.GustoPremium("Cioccolato Extra", 2.0, ["latte"], ["scaglie fondenti"], 0.7)

    # Gusto vegano -> nome: str, prezzo_base: float, allergeni: list, base_vegetale: str
    v1 = gusto.GustoVegano("Cocco Tropicale", 2.2, ["nessuno"], "latte di cocco")

    # Aggiungo al menu
    menu.aggiungi_gusto(g1)
    menu.aggiungi_gusto(g2)
    menu.aggiungi_gusto(g3)
    menu.aggiungi_gusto(p1)
    menu.aggiungi_gusto(p2)
    menu.aggiungi_gusto(v1)

    # MENU UTENTE
    while True:
        print("\nSCEGLI UN'OPERAZIONE:")
        print("(1) Mostra menu gelateria")
        print("(2) Aggiungi gusto base")
        print("(3) Aggiungi gusto premium")
        print("(4) Aggiungi gusto vegano")
        print("(5) Rimuovi un gusto")
        print("(0) Esci")

        scelta = input("\nScelta (0-5): ")

        match scelta:
            case "1":
                menu.lista_gusti()

            case "2":
                nome = input("\nNome gusto: ")
                prezzo = float(input("Prezzo base: "))
                allergeni = input("Allergeni (separati da virgola): ").split(",")
                allergeni = [a.strip() for a in allergeni]

                nuovo = gusto.Gusto(nome, prezzo, allergeni)
                menu.aggiungi_gusto(nuovo)
                print("\nGusto base aggiunto!\n")

            case "3":
                nome = input("\nNome gusto premium: ")
                prezzo = float(input("Prezzo base: "))
                allergeni = input("Allergeni (separati da virgola): ").split(",")
                ingredienti = input("Ingredienti speciali (separati da virgola): ").split(",")
                sovrapprezzo = float(input("Sovrapprezzo: "))

                allergeni = [a.strip() for a in allergeni]
                ingredienti = [i.strip() for i in ingredienti]

                nuovo = gusto.GustoPremium(nome, prezzo, allergeni, ingredienti, sovrapprezzo)
                menu.aggiungi_gusto(nuovo)
                print("\nGusto premium aggiunto!\n")

            case "4":
                nome = input("\nNome gusto vegano: ")
                prezzo = float(input("Prezzo base: "))
                allergeni = input("Allergeni (separati da virgola): ").split(",")
                base_veg = input("Tipo base vegetale (es. soia, mandorla, cocco): ")

                allergeni = [a.strip() for a in allergeni]

                nuovo = gusto.GustoVegano(nome, prezzo, allergeni, base_veg)
                menu.aggiungi_gusto(nuovo)
                print("\nGusto vegano aggiunto!\n")

            case "5":
                nome = input("\nNome del gusto da rimuovere: ")
                menu.rimuovi_gusto(nome)

            case "0":
                print("\nUscita.")
                break

            case _:
                print("\nScelta non valida.")
                
if __name__ == "__main__":
    main()