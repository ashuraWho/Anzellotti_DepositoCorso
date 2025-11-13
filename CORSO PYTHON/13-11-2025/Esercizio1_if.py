print("\n***************************************************")
print("*** Benvenuto nella piattaforma di visione film ***")
print("***************************************************")
comando = input("\nInserisci un comando (start, stop): ")

match comando:
    case "start":
        print("\nAvvio della piattaforma.")
        
        eta = int(input("\nInserisci la tua età: "))
        if eta < 18:
            print("Accesso negato. Devi essere almeno 18 anni per accedere ai contenuti.")
            print("Mi dispiace, non puoi vedere questo film.")
        else:
            print("Accesso consentito. Puoi vedere questo film. Buona visione!")
        
    case "stop":
        print("\nChiusura della piattaforma.")
        
    case _:
        print("\nComando non riconosciuto.")