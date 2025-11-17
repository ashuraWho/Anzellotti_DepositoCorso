# --------------------------------------------------------------
# ---------- MODULO: ANALIZZATORE DI DATI DI VENDITA -----------
# --------------------------------------------------------------

class Analizzatore:
    
    def __init__(self, vendite):
        self.vendite = vendite  # lista di interi
        
    def totale(self):
        return sum(self.vendite)
    
    def media(self):
        
        if len(self.vendite) == 0:
            return 0
        
        return self.totale() / len(self.vendite)
    
    def sopra_media(self):
        result = []
        mean = self.media()

        for giorno, value in enumerate(self.vendite):
            if value > mean:
                result.append((giorno + 1, value)) # giorno +1 così il giorno parte da 1

        return result