import studenti as st

# Creo alcune istanze: Studenti e Professori
s1 = st.Studente("Mario Verdi", 16, [8, 7, 9])
s2 = st.Studente("Bruno Neri", 17)  # senza voti iniziali
p1 = st.Professore("Dr. Carla Bianchi", 45, "Matematica")

# Aggiungo voti a s2
s2.aggiungi_voto(6)
s2.aggiungi_voto(7)

persone = [s1, s2, p1]

while True:
    print("\n--- MENU ---")
    print("(1) Mostra presentazioni")
    print("(2) Mostra dati con getter/setter")
    print("(3) Test eccezioni (set_eta)")
    print("(4) Test eccezioni (set_materia)")
    print("(0) Esci")

    scelta = input("\nScelta (0-4): ")

    match scelta:
        case "1":
            print("\n--- Presentazioni ---")
            for persona in persone:
                persona.presentazione()

        case "2":
            print("\n--- Accesso tramite getter/setter ---")
            print("Nome studente s1:", s1.get_nome())
            print("Età professore p1:", p1.get_eta())
            print("Materia p1:", p1.get_materia())
            print("Voti s1:", s1.get_voti())
            print("Media s1:", s1.calcola_media())

        case "3":
            print("\n--- Test eccezione set_eta ---")
            s1.set_eta(-5)  # Genera ValueError

        case "4":
            print("\n--- Test eccezione set_materia ---")
            p1.set_materia("")  # Genera ValueError

        case "0":
            print("Uscita.")
            break

        case _:
            print("Scelta non valida.")