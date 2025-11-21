import permits as per
import staff as st

"""
    Ho scritto le cose in inglese perché nell'azienda potrebbero lavorarci delle persone straniere.
    Non ho fatto in tempo a fare l'inserimento in input.
    
"""

def main():
    ac = per.AccessController()

    # Creazione persone e badge già pronti
    b1 = st.Badge("B1")
    b2 = st.Badge("B2")
    b3 = st.Badge("V1")
    b4 = st.Badge("B3")

    # Persone: 2 dipendenti, 1 menager e 1 visitatore
    emp1 = st.Employee("Luca", "Developer")
    emp1.assign_badge(b1)
    emp1.add_permission("lab")

    emp2 = st.Employee("Sara", "Designer")
    emp2.assign_badge(b4)
    emp2.add_permission("office")

    mgr = st.Manager("Anna")
    mgr.assign_badge(b2)

    visitor = st.Visitor("Gino", valid_seconds=3600)
    visitor.assign_badge(b3)

    # Lista di persone
    people = [emp1, emp2, mgr, visitor]

    # Menu interattivo
    while True:
        print("\n--- Workplace Entry Management ---")
        print("(1) Show people")
        print("(2) Request access to an area")
        print("(3) Show access log")
        print("(0) Exit")
        choice = input("\nOption (0-3): ")

        if choice == "1":
            print("\nPeople present:")
            for idx, p in enumerate(people): # Uso enumerate() così mi dà indice ed elemento
                print(f"{idx+1}) {p.get_name()} ({p.__class__.__name__})")

        elif choice == "2":
            print("\nSelect person:")
            for idx, p in enumerate(people):
                print(f"({idx+1}) {p.get_name()}")
            try:
                sel = int(input("Number of person: ")) - 1
                if sel < 0 or sel >= len(people):
                    print("Invalid input.")
                    continue
                person = people[sel]
                area = input("Enter the area to access (office, server, lab, reception): ").lower()
                
                # Match per stampa messaggio in base a risultato
                granted = ac.request_access(person, area)
                match granted:
                    case True:
                        print(f"Access granted to {person.get_name()} for {area}")
                    case False:
                        print(f"Access denied to {person.get_name()} for {area}")
            except ValueError:
                print("Invalid input.")

        elif choice == "3":
            print("\nAccess log")
            for entry in ac.get_log():
                print(entry)

        elif choice == "0":
            print("Exit.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()