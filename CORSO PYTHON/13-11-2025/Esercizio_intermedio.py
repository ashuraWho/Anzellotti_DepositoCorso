# --------------------------------------------------------------
# ---------------- NUMERI PRIMI IN UN INTERVALLO ---------------
# --------------------------------------------------------------

ripetere = True

while ripetere:
    risposta = input("\nVuoi trovare i numeri primi in un intervallo? (si/no): ")
    
    if risposta.lower() == 'no':
         ripetere = False
         print("\nUscita dal programma.")
        
    elif risposta.lower() == 'si':
        print("\nInserisci l'intervallo per trovare i numeri primi.")
        minimo = int(input("Valore minimo: "))
        massimo = int(input("Valore massimo: "))
        
        while minimo >= massimo:
            print("\nIntervallo non valido. Il valore minimo deve essere inferiore al valore massimo.")
            minimo = int(input("Valore minimo: "))
            massimo = int(input("Valore massimo: "))

        primi = [] # lista per i numeri primi
        non_primi = [] # lista per i numeri non primi

        for num in range(minimo, massimo + 1):
            if num == 1:
                non_primi.append(num)
            elif num > 1:
                for i in range(2, int(num**0.5) + 1):
                    if num % i == 0:
                        non_primi.append(num)
                        break
                else: # per for non per if (se non avviene il break)
                    primi.append(num)
        
        primi.sort()
        non_primi.sort()
        print(f"\n(1) Numeri primi tra {minimo} e {massimo}: {primi}")
        print(f"\n(2) Numeri non primi tra {minimo} e {massimo}: {non_primi}")
        
        print("\n--------------------------------")
        
        scelta = input("\nVuoi ripetere? (si/no): ")
        while scelta.lower() not in ['si', 'no']:
            scelta = input("Risposta non valida. Per favore rispondi con 'si' o 'no': ")
        
        if scelta.lower() == 'no':
            ripetere = False
            print("\nUscita dal programma.")

    else:
        print("\nRisposta non valida. Per favore rispondi con 'si' o 'no'.")

