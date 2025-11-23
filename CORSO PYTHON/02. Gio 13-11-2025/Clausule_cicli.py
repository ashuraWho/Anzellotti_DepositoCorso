# --------------------------------------------------------------
# ---------------------------- break ---------------------------
# --------------------------------------------------------------

numeri = [1, 2, 3, 4, 5]

for numero in numeri:
    if numero == 3:
        print("\nTrovato il numero 3, interrompo il ciclo.")
        break # Interrompe il ciclo quando trova il numero 3
    print(f"\nNumero attuale: {numero}")

print("\n--------------------------------")

# --------------------------------------------------------------
# -------------------------- continue --------------------------
# --------------------------------------------------------------

for numero in numeri:
    if numero == 3:
        print("\nSaltando il numero 3.")
        continue # Salta il numero 3 e continua con il ciclo
    print(f"\nNumero attuale: {numero}")
    
print("\nCiclo completato.")

print("\n--------------------------------")

# --------------------------------------------------------------
# ---------------------------- pass ----------------------------
# --------------------------------------------------------------

for i in range(5):
    if i == 3:
        pass # Non fa nulla quando i è 3
    print(f"\nIndice attuale: {i}")

print("\n--------------------------------")

# --------------------------------------------------------------
# -------------------------- splat (*) -------------------------
# --------------------------------------------------------------

numeri = [*range(1, 11)] # Usa lo splat per creare una lista da un range
print(numeri)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]