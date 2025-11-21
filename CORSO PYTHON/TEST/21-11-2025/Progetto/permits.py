"""
    
    Implemento tutta la logica per gestire richieste di accesso
    
"""

import time # Lo utilizzavo in alcuni codici ad astrofisica

class AccessController: # Per gestire le richieste di accesso
    def __init__(self):
        self._log = []  # Registro

    def request_access(self, person, area): # Controllo badge e permessi
        
        if not person._badge or not person._badge.active:
            granted = False # Concessione negata
        else:
            granted = person.can_access(area)

        # Registra l'evento nel registro
        entry = (time.strftime("%Y-%m-%d %H:%M:%S"), person.get_name(), area, granted) # Mi dà la data tipo "2025-11-21 12:41:57"
        self._log.append(entry)
        return granted

    def get_log(self):
        return list(self._log)

    def clear_log(self):
        self._log = []