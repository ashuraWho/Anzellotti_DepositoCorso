print("\n********************")
print("*** CALCOLATRICE ***")
print("********************")

x = float(input("\nInserisci il primo numero: "))
y = float(input("Inserisci il secondo numero: "))

operazione = input("\nScegli l'operazione (+, -, *, /, **): ")

match operazione:
    case "+":
        print(f"\n{x} + {y} = {x + y}")
        
    case "-":
        print(f"\n{x} - {y} = {x - y}")
        
    case "*":
        print(f"\n{x} * {y} = {x * y}")
        
    case "/":
        if y != 0:
            print(f"\n{x} / {y} = {x / y}")
        else:
            print("\nErrore: Divisione per zero non consentita.")
            
    case "**":
        if (x*y) < 0 and y % 1 != 0:
            print("\nErrore: Non è possibile elevare un numero negativo a una potenza frazionaria.")
        else:
            print(f"\n{x} ** {y} = {x ** y}")
        
    case _:
        print("\nOperazione non valida.")