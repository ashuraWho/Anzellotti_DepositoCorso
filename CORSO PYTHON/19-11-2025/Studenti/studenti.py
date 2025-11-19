class Persona: # Classe base -> persona generica.
    
    """
    Incapsulamento: gli attributi sono privati.
    Fornisce getter e setter per nome ed eta.
    """
    
    def __init__(self, nome, eta):
        # Attributi privati
        self.__nome = None
        self.__eta = None

        # Inizializzo
        self.set_nome(nome)
        self.set_eta(eta)

    # NOME
    def get_nome(self): # Restituisce il nome della persona (str)
        return self.__nome

    def set_nome(self, nuovo_nome): # Imposta il nome della persona
        if not isinstance(nuovo_nome, str) or nuovo_nome.strip() == "":
            print("\nIl nome deve essere una stringa non vuota.")
        else:
            self.__nome = nuovo_nome.strip()

    # ETA'
    def get_eta(self): # Restituisce l'età della persona (int)
        return self.__eta

    def set_eta(self, nuova_eta):
        if not isinstance(nuova_eta, int) or nuova_eta < 0:
            print("\nL'età deve essere un intero >= 0.")
        else:
            self.__eta = nuova_eta

    def presentazione(self):
        print(f"Mi chiamo {self.get_nome()} e ho {self.get_eta()} anni.")


# -----------------------------------------------------
# Sottoclasse 'Studente' che eredita da 'Persona'
class Studente(Persona):

    def __init__(self, nome, eta, voti=None):
        super().__init__(nome, eta)

        self.__voti = []

        # Se viene fornita una lista di voti, la imposto tramite setter
        if voti is None:
            voti = []
        self.set_voti(voti)

    def get_voti(self):
        return list(self.__voti)

    def set_voti(self, nuova_lista_voti):
        if not isinstance(nuova_lista_voti, list):
            print("\nI voti devono essere passati come lista.")
        else:
            for v in nuova_lista_voti:
                if not isinstance(v, int) or v < 0 or v > 10:
                    print("\nOgni voto deve essere un intero tra 0 e 10.")
            
            self.__voti = list(nuova_lista_voti)  # memorizzo una copia

    def aggiungi_voto(self, voto):
        if not isinstance(voto, int) or voto < 0 or voto > 10:
            print("\nIl voto deve essere un intero tra 0 e 10.")
        else:
            self.__voti.append(voto)

    def calcola_media(self):
        if len(self.__voti) == 0:
            return None
        
        return sum(self.__voti) / len(self.__voti)

    def presentazione(self):
        media = self.calcola_media()
        if media is None:
            print(f"Mi chiamo {self.get_nome()}, ho {self.get_eta()} anni e non ho ancora voti.")
        else:
            print(f"Mi chiamo {self.get_nome()}, ho {self.get_eta()} anni. Media voti: {media:.2f}.")

# -----------------------------------------------------
# Sottoclasse 'Professore' che eredita da 'Persona'
class Professore(Persona):
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)
        
        self.__materia = None
        self.set_materia(materia)

    def get_materia(self):
        return self.__materia

    def set_materia(self, nuova_materia):
        if not isinstance(nuova_materia, str) or nuova_materia.strip() == "":
            print("\nLa materia deve essere una stringa non vuota.")
        else:
            self.__materia = nuova_materia.strip()

    def presentazione(self):
        print(f"Mi chiamo {self.get_nome()}, ho {self.get_eta()} anni e insegno {self.get_materia()}.")