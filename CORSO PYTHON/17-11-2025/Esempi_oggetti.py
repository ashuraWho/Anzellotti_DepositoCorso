# --------------------------------------------------------------
# --------------------------- OGGETTI --------------------------
# --------------------------------------------------------------

# Una CLASSE è un blue print (un modello progettuale)
# (1) Le classi sono definite usando la parola chiave class, seguita dal nome della classe
# (2) Definisce le variabili (attributi) e i comportamenti (metodi) che può fare un singolo oggetto

# Un OGGETTO è un'istanza di una classe, cioè una copia univoca della classe che ha le sue proprietà uniche
# (1) Può solo fare quanto definito dalla classe

# UNA classe con (potenziali) INFINITI oggetti

# ----------------------------------------------------------------------

# Gli ATTRIBUTI sono variabili associate a una classe
# (1) Rappresentano le proprietà di un oggetto
# (2) Sono condivisi tra tutte le istanze della classe

# I METODI sono funzioni associate a una classe
# (1) Rappresentano il comportamento di un oggetto
# (2) Metodo SPECIALE/SUBORDINATO:
#
#      - COSTRUTTORE: __init__
#           -> Il costruttore è un metodo speciale che viene invocato automaticamente al momento della creazione di un nuovo oggetto
#           -> Serve ad inizializzare l'oggetto appena creato, impostando attributi e valori iniziali
#           -> Accetta sempre almeno il parametro self (che rappresenta l'istanza corrente)
#           -> Può accettare ulteriori parametri per la configurazione iniziale
#
#      - STAMPA: __str__

# ----------------------------------------------------------------------

# ----- I 3 TIPI DI METODI: -----

# I metodi sono funzioni definite all'interno di una classe che operano sugli oggetti (le istanze) della classe stessa.

# (1) Metodi di ISTANZA (quelli base): Operano su un'istanza specifica e accedono ai dati dell'oggetto tramite self.

class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome}")

p = Persona("Luca", 25) # Creazione di un oggetto Persona
p.saluta() # Output: Ciao, mi chiamo Luca 

"""

    Metodo di Istanza (senza decoratore):
    
    - Definito senza decoratori particolari.
    - Riceve come primo parametro l'istanza (self).
    - Opera sui dati specifici di quell'istanza.

"""

# -------

# (2) Metodi di CLASSE: Operano sulla classe e non su un'istanza specifica.
# -> Sono definiti usando il decoratore @classmethod e ricevono come primo parametro la classe (cls).

class Contatore:
# Il metodo mostra_numero_istanze è un metodo di classe e utilizza:
# - il decoratore @classmethod
# - il parametro cls rappresenta la classe stessa e permette di accedere ad attributi di classe

    numero_istanze = 0  # Attributo di classe

    def __init__(self):
        Contatore.numero_istanze += 1

    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")

c1 = Contatore() # Creazione di alcune istanze
c2 = Contatore() # Creazione di alcune istanze

Contatore.mostra_numero_istanze() # Output: Sono state create 2 istanze.

"""
        
    --- @classmethod Caratteristiche: ---

    - Riceve un riferimento alla classe: Un metodo di classe
    riceve come primo parametro la classe stessa (di convenzione cls).
    Ciò consente di accedere e modificare attributi e metodi della classe.
    
    - Polimorfismo e ereditarietà: Permette di creare metodi
    che funzionano in maniera diversa a seconda della classe in cui 
    vengono invocati, rendendoli particolarmente utili nelle gerarchie di classi.
    
    - Chiamata: Può essere chiamato sia tramite la classe sia tramite un'istanza,
    ma il primo parametro sarà sempre la classe.

    --- Quando usarlo? ---

    Utilizza un metodo di classe quando hai bisogno di:
    (1) Accedere o modificare gli attributi di classe.
    (2) Creare metodi che creano e restituiscono nuove istanze 
    della classe che possono essere sovrascritti nelle classi derivate (ereditarietà).

"""

# -------

# (3) Metodi STATICI: Funzioni legate alla classe ma che non operano né sull'istanza né sulla classe.
# -> Sono definiti con il decoratore @staticmethod.

class Calcolatrice:
# Il metodo somma è un metodo statico, quindi non riceve né "self" né "cls" come parametro e può essere invocato direttamente dalla classe.

    @staticmethod
    def somma(a, b):
        return a + b

risultato = Calcolatrice.somma(5, 3) # Uso del metodo statico senza creare un'istanza
print(risultato) # Output: 8

"""

    --- @staticmethod   Caratteristiche: ---

    - Nessun riferimento implicito: Un metodo statico
    non riceve automaticamente un riferimento
    all'istanza (self) né alla classe (cls).
    
    - Funzione indipendente: Può essere considerato
    come una funzione ordinaria definita all'interno
    della classe, utile per raggruppare logicamente
    operazioni che riguardano la classe ma che non
    necessitano di accedere a dati di istanza o di
    classe.
    
    - Chiamata: Può essere chiamato sia tramite
    l'istanza sia direttamente dalla classe.

    --- Quando usarlo? ---

    Utilizza un metodo statico quando la funzione non
    ha bisogno di accedere o modificare lo stato della
    classe o dell'istanza. È una scelta ideale per
    funzioni di utilità che sono logicamente collegate
    alla classe

"""

# ----------------------------------------------------------------------

# Creazione di una classe
class Automobile: # dichiaro la classe

    numero_di_ruote = 4 # ATTRIBUTO di classe

    def __init__(self, marca, modello): # metodo COSTRUTTORE: serve a costruire l'oggetto (serve a dire: "se vuoi una macchina devi darmi questi valori")

        # Il "self" è un parametro per convenzione che viene utilizzato dal nome reale dell'oggetto
        self.marca = marca # attributo di ISTANZA
        self.modello = modello # attributo di ISTANZA

    def stampa_info(self): # metodo di ISTANZA

        print("L'automobile è una", self.marca, self.modello)
        
# Creazione di oggetti da una classe
auto1 = Automobile("Fiat", "500") # crea un oggetto di Automobile
auto2 = Automobile("BMW", "X3") # crea un altro oggetto di Automobile
# -> il "self" non viene mai messo nei parametri perché è il nome stesso - qui è "auto1" e "auto2"

auto1.stampa_info() # stampa "L'automobile è una Fiat 500"
auto2.stampa_info() # stampa "L'automobile è una BMW X3"

# -> Un oggetto della classe "Automobile" è di tipo "Automobile"
# -> è un TIPO NON-BASILARE, ovvero quei tipi che definiamo noi

# ----------------------------------------------------------------------

# CLASSE "Persona" con METODO "__str__"
"""

    Rappresenta una persona, con nome ed età.
    Il metodo __str__ restituisce una stringa descrittiva dell'oggetto.

"""
class Persona:
    
    def __init__(self, nome, eta):
        self.nome = nome   # Attributo per memorizzare il nome
        self.eta = eta     # Attributo per memorizzare l'età
        
    def __str__(self):
        # Viene richiamato quando facciamo: print(istanza_di_Persona)
        return f"Persona(nome={self.nome}, eta={self.eta})"

# Creazione di un oggetto Persona
p = Persona("Pippo", 30)

print(p.nome)  # Output: Pippo
print(p.eta)   # Output: 30