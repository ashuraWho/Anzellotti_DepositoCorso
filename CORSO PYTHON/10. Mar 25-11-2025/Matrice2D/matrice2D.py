import numpy as np
import salva_su_file as salva

def crea_matrice(logfile):
    try:
        righe = int(input("\nInserisci il numero di righe: "))
        colonne = int(input("Inserisci il numero di colonne: "))
        range_min = int(input("Inserisci il valore minimo: "))
        range_max = int(input("Inserisci il valore massimo: "))
        matrice = np.random.randint(range_min, range_max, (righe, colonne))
        
        """
            Con:
                matrice = np.random.randint(0, 100, (righe, colonne))
                
            Vado a sostituire:
                arr_rand = np.random.random(n) * (rand_max - rand_min) + rand_min
                arr_rand = arr_rand.astype(int)
                arr_rand = arr_rand.reshape(righe, colonne)
        """
        print("\nMatrice generata:\n", matrice)
        salva.salvaFile(f"Nuova matrice:\n{matrice}", logfile)
        
        return matrice
    
    except ValueError:
        print("\nERRORE: inserisci valori numerici validi.")
        return None

# ----------------------------------------------------------------

def sotto_matrice_centrale(matrice, logfile):
    if matrice is None:
        print("\nNessuna matrice presente.")
        return

    r, c = matrice.shape
    if r < 3 or c < 3:
        print("Per la sotto-matrice centrale devo avere una matrice 3x3.")
        return
    
    sub = matrice[1:-1, 1:-1]
        
    print("\nSotto-matrice centrale:\n", sub)
    salva.salvaFile(f"Sotto-matrice centrale:\n{sub}", logfile)
    
    return sub

# ----------------------------------------------------------------

def trasposta(matrice, logfile):
    if matrice is None:
        print("\nNessuna matrice presente.")
        return

    print("\nMatrice trasposta:\n", matrice.T)
    salva.salvaFile(f"Matrice trasposta:\n{matrice.T}", logfile)
    
    return matrice.T

# ----------------------------------------------------------------

def somma(matrice, logfile):
    if matrice is None:
        print("\nNessuna matrice presente.")
        return

    print("\nSomma di tutti gli elementi:", matrice.sum())
    print("\nSomma di tutti gli elementi:\n", matrice.sum())
    salva.salvaFile(f"Somma di tutti gli elementi:\n{matrice.sum()}", logfile)
    
    return matrice.sum()

# ----------------------------------------------------------------

def elementwise(matrice, logfile):
    range_min = int(input("Inserisci il valore minimo: "))
    range_max = int(input("Inserisci il valore massimo: "))
    matrice2 = np.random.randint(range_min, range_max, matrice.shape)

    print("Seconda matrice:\n", matrice2)
    print("\nRisultato moltiplicazione elemento per elemento:\n", matrice * matrice2)
    salva.salvaFile(f"Moltiplicazione element-wise:\n{matrice * matrice2}", logfile)
    
    return matrice * matrice2

# ----------------------------------------------------------------

def media(matrice, logfile):
    media = np.mean(matrice)
    print("\nMedia degli elementi =", media)
    salva.salvaFile(f"Media degli elementi: {media}", logfile)
    
    return media

# ----------------------------------------------------------------

def determinante(matrice, logfile):
    if matrice.shape[0] != matrice.shape[1]:
        print("La matrice non è quadrata, impossibile calcolare il determinante.")
        return None

    det = np.linalg.det(matrice) # Calcola il determinante
    print("\nDeterminante =", det)
    salva.salvaFile(f"Determinante: {det}", logfile)
    
    return det
