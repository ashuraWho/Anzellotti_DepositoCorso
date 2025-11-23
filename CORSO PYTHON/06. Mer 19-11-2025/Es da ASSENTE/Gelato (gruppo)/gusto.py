# CLASSE BASE
class Gusto: # Rappresenta un gusto semplice di gelato
    
    def __init__(self, nome: str, prezzo_base: float, allergeni: list):
        # Attributi privati
        self.__nome = nome
        self.__prezzo_base = prezzo_base # Prezzo singola pallina
        self.__allergeni = allergeni # Lista di stringhe

    # getter e setter
    def get_nome(self):
        return self.__nome

    def set_nome(self, nuovo_nome):
        self.__nome = nuovo_nome

    def get_prezzo(self):
        return self.__prezzo_base

    def set_prezzo(self, nuovo_prezzo):
        self.__prezzo_base = nuovo_prezzo

    def get_allergeni(self):
        return self.__allergeni

    def set_allergeni(self, nuova_lista):
        self.__allergeni = nuova_lista

    def descrizione(self):
        return (f" * {self.__nome} "
                f"- prezzo: {self.__prezzo_base}€ "
                f"- allergeni: {', '.join(self.__allergeni)}")


# SOTTOCLASSE
class GustoPremium(Gusto): # Aggiunge ingredienti speciali e sovrapprezzo
    
    def __init__(self, nome: str, prezzo_base: float, allergeni: list, ingredienti_speciali: list, sovrapprezzo: float):
        super().__init__(nome, prezzo_base, allergeni)
        
        self.__ingredienti_speciali = ingredienti_speciali # Lista di stringhe
        self.__sovrapprezzo = sovrapprezzo

    def descrizione_premium(self):
        prezzo_finale = self.get_prezzo() + self.__sovrapprezzo
        return (
            f" * {self.get_nome()} (Premium) "
            f"- prezzo: {prezzo_finale}€ "
            f"- ingredienti speciali: {', '.join(self.__ingredienti_speciali)} "
            f"- allergeni: {', '.join(self.get_allergeni())}"
        )


class GustoVegano(Gusto): # Aggiunge il tipo di base vegetale
    
    def __init__(self, nome: str, prezzo_base: float, allergeni: list, base_vegetale: str):
        super().__init__(nome, prezzo_base, allergeni)
        
        self.__base_vegetale = base_vegetale

    def descrizione_vegano(self):
        return (
            f" * {self.get_nome()} (Vegano) "
            f"- prezzo: {self.get_prezzo()}€ "
            f"- base: {self.__base_vegetale} "
            f"- allergeni: {', '.join(self.get_allergeni())}"
        )