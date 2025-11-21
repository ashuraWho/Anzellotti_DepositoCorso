"""
    
    Implemento tutta la logica per i Badge e le persone che entrano in azienda:
        - dipendenti
        - menager
        - eventuali visitatori: qui sarebbe stato figo anche mettere il temopo in ingresso
            e quello di uscita per avere un badge limitato, ma non so come si fa
    
"""
import time # Lo utilizzavo in alcuni codici ad astrofisica

class Badge: # Badge assegnato ad una persona
    def __init__(self, badge_id):
        self.id = badge_id # ID badge
        self.active = True # Stato badge: attivo/non attivo

    def deactivate(self): # Disattivo il badge
        self.active = False

# ---------------------------------------------------------------

class Person: # Classe base
    def __init__(self, name):
        self._name = name
        self._badge = None # Badge assegnato

    def assign_badge(self, badge):
        self._badge = badge

    def get_name(self): # Leggere il nome
        return self._name

    def can_access(self, area): # Questo sta qui giusto per essere ridefinito dopo
        return False

# ---------------------------------------------------------------

class Employee(Person): # Classe figlio di "Person" (per i dipendenti)
    def __init__(self, name, role):
        super().__init__(name)
        
        self.role = role # Ruolo del dipendente
        self.permissions = ["office"]  # Aree dove il dipendente può accedere (di base è l"ufficio)

    def add_permission(self, area): # Aggiunge un"area ai permessi
        if area not in self.permissions:
            self.permissions.append(area)

    def can_access(self, area): # Uso il polimorfismo dato che sto ridefinendo il metodo del padre
        if not self._badge or not self._badge.active: # Se non ha il badge o è disattivo -> accesso negato
            return False
        
        return area in self.permissions


class Manager(Employee): # Classe figlio di "Employee" (per i menager) -> i menager sono dipendenti, solo che hanno più permessi
    def __init__(self, name):
        super().__init__(name, role="Manager")
        self.permissions = ["office", "server", "lab"]

    def can_access(self, area): # Qui metto che il menager può accedere ovunque
        if not self._badge or not self._badge.active: # Se non ha il badge o è disattivo -> accesso negato
            return False
        
        return True


class Visitor(Person): # Classe figlio di "Person" (per i visitatori) -> se magari il tipo di azienda permetta la visita di visitatori
    def __init__(self, name, valid_seconds = 7200): # Permesso di default 2 ore
        super().__init__(name)
        self.allowed_areas = ["reception"] # Ovviamente i visitatori hanno maggiori restrizioni -> solo la reception se c"è
        self._start_time = time.time()  # Orario corrente in secondi
        self._valid_seconds = valid_seconds  # Durata del badge in secondi

        
    def can_access(self, area):
        current_time = time.time() # L"orario corrente
        
        if not self._badge or not self._badge.active:
            return False
        if current_time - self._start_time > self._valid_seconds:
            return False
        
        return area in self.allowed_areas