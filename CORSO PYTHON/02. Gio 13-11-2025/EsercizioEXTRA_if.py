print("\n********************")
print("*** CALCOLATRICE ***")
print("********************")

print("Le operazioni disponibili sono: +, -, *, /, **")
print("Nota: L'operazione verrà eseguita in questo modo:")
print("\nSOMMA: x + y ; x + y + z ; x + y + z + h ; x + y + z + h + k")
print("SOTTRAZIONE: x - y ; x - y - z ; x - y - z - h ; x - y - z - h - k")
print("MOLTIPLICAZIONE: x * y ; x * y * z ; x * y * h ; x * y * z * h * k")
print("DIVISIONE: x / y ; x / y / z ; x / y / z / h ; x / y // z / h / k")
print("POTENZA: x ** y ; x ** y ** z ; x ** y ** z ** h ; x ** y ** z ** h ** k")

# Richiesta del numero di valori da inserire
num_valori = int(input("\nQuanti valori vuoi inserire (2-5)? "))

if num_valori == 2:
    x = float(input("\nInserisci il primo numero: "))
    y = float(input("Inserisci il secondo numero: "))
    input_lista = [x, y]

elif num_valori == 3:
    x = float(input("\nInserisci il primo numero: "))
    y = float(input("Inserisci il secondo numero: "))
    z = float(input("Inserisci il terzo numero: "))
    input_lista = [x, y, z]

elif num_valori == 4:
    x = float(input("\nInserisci il primo numero: "))
    y = float(input("Inserisci il secondo numero: "))
    z = float(input("Inserisci il terzo numero: "))
    h = float(input("Inserisci il quarto numero: "))
    input_lista = [x, y, z, h]

elif num_valori == 5:
    x = float(input("\nInserisci il primo numero: "))
    y = float(input("Inserisci il secondo numero: "))
    z = float(input("Inserisci il terzo numero: "))
    h = float(input("Inserisci il quarto numero: "))
    k = float(input("Inserisci il quinto numero: "))
    input_lista = [x, y, z, h, k]
    
else:
    print("\nPuoi inserire al massimo 5 valori.")
    exit()

print("\nI numeri inseriti sono:", input_lista)

operazione = input("\nScegli l'operazione (+, -, *, /, **): ")

match operazione:
    case "+":
        if num_valori == 2:
            print(f"\n{x} + {y} = {x + y}")
        elif num_valori == 3:
            print(f"\n{x} + {y} + {z} = {x + y + z}")
        elif num_valori == 4:
            print(f"\n{x} + {y} + {z} + {h} = {x + y + z + h}")
        elif num_valori == 5:
            print(f"\n{x} + {y} + {z} + {h} + {k} = {x + y + z + h + k}")
        
    case "-":
        if num_valori == 2:
            print(f"\n{x} - {y} = {x - y}")
        elif num_valori == 3:
            print(f"\n{x} - {y} - {z} = {x - y - z}")
        elif num_valori == 4:
            print(f"\n{x} - {y} - {z} - {h} = {x - y - z - h}")
        elif num_valori == 5:
            print(f"\n{x} - {y} - {z} - {h} - {k} = {x - y - z - h - k}")
        
    case "*":
        if num_valori == 2:
            print(f"\n{x} * {y} = {x * y}")
        elif num_valori == 3:
            print(f"\n{x} * {y} * {z} = {x * y * z}")
        elif num_valori == 4:
            print(f"\n{x} * {y} * {z} * {h} = {x * y * z * h}")
        elif num_valori == 5:
            print(f"\n{x} * {y} * {z} * {h} * {k} = {x * y * z * h * k}")
        
    case "/":
        if num_valori == 2:
            if y != 0:
                print(f"\n{x} / {y} = {x / y}")
            else:
                print("\nErrore: Divisione per zero non consentita.")
        elif num_valori == 3:
            if y != 0 and z != 0:
                print(f"\n{x} / {y} / {z} = {x / y / z}")
            else:
                print("\nErrore: Divisione per zero non consentita.")
        elif num_valori == 4:
            if y != 0 and z != 0 and h != 0:
                print(f"\n{x} / {y} / {z} / {h} = {x / y / z / h}")
            else:
                print("\nErrore: Divisione per zero non consentita.")
        elif num_valori == 5:
            if y != 0 and z != 0 and h != 0 and k != 0:
                print(f"\n{x} / {y} / {z} / {h} / {k} = {x / y / z / h / k}")
            else:
                print("\nErrore: Divisione per zero non consentita.")
            
    case "**":
        if num_valori == 2:
            if (x*y) < 0 and y % 1 != 0:
                print("\nErrore: Non è possibile elevare un numero negativo a una potenza frazionaria.")
            else:
                print(f"\n{x} ** {y} = {x ** y}")
        elif num_valori == 3:
            if (x*y*z) < 0 and y % 1 != 0 and z % 1 != 0:
                print("\nErrore: Non è possibile elevare un numero negativo a una potenza frazionaria.")
            else:
                print(f"\n{x} ** {y} ** {z} = {x ** y ** z}")
        elif num_valori == 4:
            if (x*y*z*h) < 0 and y % 1 != 0 and z % 1 != 0 and h % 1 != 0:
                print("\nErrore: Non è possibile elevare un numero negativo a una potenza frazionaria.")
            else:
                print(f"\n{x} ** {y} ** {z} ** {h} = {x ** y ** z ** h}")
        elif num_valori == 5:
            if (x*y*z*h*k) < 0 and y % 1 != 0 and z % 1 != 0 and h % 1 != 0 and k % 1 != 0:
                print("\nErrore: Non è possibile elevare un numero negativo a una potenza frazionaria.")
            else:
                print(f"\n{x} ** {y} ** {z} ** {h} ** {k} = {x ** y ** z ** h ** k}")
        
    case _:
        print("\nOperazione non valida.")