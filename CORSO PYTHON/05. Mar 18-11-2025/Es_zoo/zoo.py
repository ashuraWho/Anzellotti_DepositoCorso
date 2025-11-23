# --------------------------------------------------------------
# ------------------------- MODULO: ZOO ------------------------
# --------------------------------------------------------------

class Animale: # Classe base
    def __init__(self, nome : str, eta : int):
        """
        Args:
            nome (str): nome animale
            eta (int): età animale
        """
        self.nome = nome
        self.eta = eta
    
    def fai_suono(self): # Metodo
        print(f"{self.nome} fa suono generico.")
        
# --------------------------------------------------------------
        
# Classi figlie
class Cane(Animale):
    def __init__(self, nome : str, eta : int, addestrato : bool):
        
        """
        Args:
            nome (str): nome cane
            eta (int): età cane
            addestrato (bool): se è addestrato o meno
        """
        
        Animale.__init__(self, nome, eta)
        self.addestrato = addestrato
        
    def addestramento(self):
        if self.addestrato:
            print(f"{self.nome} ha {self.eta} ed è addestrato!")
        else:
            print(f"{self.nome} ha {self.eta} ed NON è addestrato!")

class Gatto(Animale):
    def __init__(self, nome : str, eta : int, dorme : int):
        
        """
        Args:
            nome (str): nome gatto
            eta (int): età gatto
            dorme (int): quante ore dorme al giorno
        """
        
        Animale.__init__(self, nome, eta)
        self.dorme = dorme
    
    def riposino(self):
        print(f"{self.nome} ha {self.eta} e dorme {self.dorme} ore al giorno.")
    
class Formica(Animale):
    def __init__(self, nome : str, eta : int, ruolo : str):
        
        """
        Args:
            nome (str): nome formica
            eta (int): età formica
            ruolo (str): il suo ruolo nel formicaio
        """

        Animale.__init__(self, nome, eta)
        self.ruolo = ruolo
    
    def lavoro(self):
        print(f"{self.nome} ha {self.eta} ed un/una {self.ruolo}.")
    