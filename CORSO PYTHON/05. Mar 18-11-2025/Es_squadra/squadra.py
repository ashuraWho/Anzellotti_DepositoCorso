# --------------------------------------------------------------
# ----------------------- MODULO: SQUADRA ----------------------
# --------------------------------------------------------------

# CLASSE BASE
class MembroSquadra:
    def __init__(self, nome : str, eta : int):
        """
        Args:
            nome (str): nome membro squadra
            eta (int): età membro squadra
        """
        self.nome = nome
        self.eta = eta
    
    def descrivi(self):
        print(f"\nMembro: {self.nome} | Età: {self.eta}")
    
# CLASSI FIGLIE
class Giocatore(MembroSquadra):
    def __init__(self, nome : str, eta : int, ruolo : str, numero_maglia : int):
        
        """
        Args:
            nome (str): nome membro squadra
            eta (int): età membro squadra
            ruolo (str): ruolo membro squadra
            numero_maglia (int): numero della maglia
        """
        
        MembroSquadra.__init__(self, nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia

    def gioca_partita(self):
        self.descrivi()
        print(f"Ruolo: {self.ruolo} | Numero maglia: {self.numero_maglia}")
    
class Allenatore(MembroSquadra):
    def __init__(self, nome : str, eta : int, anni_di_esperienza : int):
        
        """
        Args:
            nome (str): nome allenatore
            eta (int): età allenatore
            anni_di_esperienza (int): anni di esperienza allenatore
        """
        
        MembroSquadra.__init__(self, nome, eta)
        self.anni_di_esperienza = anni_di_esperienza
    
    def dirige_allenamento(self):
        self.descrivi()
        print(f"Con i suoi {self.anni_di_esperienza} anni di esperienza sa perfettamente come gestire la panchina.")
        
class Assistente(MembroSquadra):
    def __init__(self, nome : str, eta : int, specializzazione : str):
        
        """
        Args:
            nome (str): nome assistente
            eta (int): età assistente
            specializzazione (str): specializzazione assistente
        """
        
        MembroSquadra.__init__(self, nome, eta)
        self.specializzazione = specializzazione
        
    def supporta_team(self):
        self.descrivi()
        print(f"E' un {self.specializzazione} di fama mondiale.")