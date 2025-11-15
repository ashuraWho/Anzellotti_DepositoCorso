# --------------------------------------------------------------
# --------------------- FUNZIONI MATEMATICHE -------------------
# --------------------------------------------------------------

# --- NUMERO PRIMO ---

""" 

 Verifica se un numero è primo:
 un numero primo è un numero naturale > 1 che è divisibile solo per 1 e per se stesso

 Args: n (int)
 Returns: bool -> True se il numero è primo, False altrimenti
 
"""

def prime(n): 
    
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
    # (1) Perché solo fino alla radice quadrata? Se n ha un divisore maggiore della radice, ne ha anche uno minore
    # (2) Perché solo numeri dispari? I pari sono già esclusi dal controllo precedente (if n % 2 == 0: return False)
        if n % i == 0:
            return False
    
    return True 

# --------------------------------------------------------------

# --- FIBONACCI ---

"""

 Calcola l'n-esimo numero della sequenza di Fibonacci:
 0, 1, 1, 2, 3, 5, 8, 13, ... -> ogni numero è la somma dei due precedenti
 
 Args: n (int) -> La posizione nella sequenza (n >= 0)
 Returns: int -> L'n-esimo numero di Fibonacci
 
"""

def fibonacci(n):
    
    if n < 0:
        raise ValueError("\nn deve essere un numero non negativo")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1): # Itera da 2 a n (incluso)
        a, b = b, a + b  # Assegnazione simultanea: (a -> b) e (b -> a + b)
    
    return b

# --------------------------------------------------------------

# --- SEQUENZA DI FIBONACCI ---

"""

 Genera una lista con i primi n numeri della sequenza di Fibonacci
 
 Args: n (int) -> La posizione nella sequenza (n >= 0)
 Returns: list -> Lista contenente i primi n numeri di Fibonacci
 
"""

def fibonacci_sequence(n):
    
    if n < 0:
        raise ValueError("n deve essere un numero non negativo")
    if n == 0:
        return [] # per n==0: restituisco una lista vuota (0 numeri)
    if n == 1:
        return [0] # per n==1: restituisco [0] (solo il primo numero)
    
    sequence = [0, 1]
    for i in range(2, n): # Itera da 2 a n-1 (escluso) -> aggiungiamo n-2 elementi perché parto con 2 elementi: [0, 1]
        sequence.append(sequence[i - 1] + sequence[i - 2])
    
    return sequence

