from vip import PostoVIP
from vip import PostoStandard
from teatro import Teatro

def main():
    teatro = Teatro()
    
    # Aggiungo alcuni posti di esempio
    teatro.aggiungi_posto(PostoVIP(1, "A", ["Lounge", "Servizio in posto"]))
    teatro.aggiungi_posto(PostoVIP(2, "A", ["VIP"]))
    teatro.aggiungi_posto(PostoStandard(1, "B", 20.0))
    teatro.aggiungi_posto(PostoStandard(2, "B", 15.0))
    teatro.aggiungi_posto(PostoStandard(3, "B", 12.5))
    
    while True:
        print("\nMENU TEATRO")
        print("1. Aggiungi posto")
        print("2. Prenota posto")
        print("3. Libera posto")
        print("4. Visualizza tutti i posti")
        print("5. Visualizza posti occupati")
        print("0. Esci")
        
        scelta = input("Scegli un'opzione (0-5): ").strip()
        
        match scelta:
            case "1":
                aggiungi_posto_input(teatro)
            case "2":
                prenota_posto_input(teatro)
            case "3":
                libera_posto_input(teatro)
            case "4":
                teatro.stampa_tutti_posti()
            case "5":
                teatro.stampa_posti_occupati()
            case "0":
                print("Arrivederci!")
                break
            case _:
                print("Opzione non valida! Scegli tra 1 e 0.")

# Faccio altre funzioni così è più leggibile il match nel main
def aggiungi_posto_input(teatro):
    print("\n--- AGGIUNGI POSTO ---")
    print("1. Posto VIP")
    print("2. Posto Standard")
    
    tipo = input("Scegli tipo posto (1-2): ").strip()
    
    match tipo:
        case "1":
            numero = int(input("Numero posto: "))
            fila = input("Fila posto: ").upper()
            servizi = input("Servizi extra (separati da virgola): ").split(",")
            servizi_extra = [s.strip() for s in servizi if s.strip()]
            
            posto = PostoVIP(numero, fila, servizi_extra)
            teatro.aggiungi_posto(posto)
            
        case "2":
            numero = int(input("Numero posto: "))
            fila = input("Fila posto: ").upper()
            costo = float(input("Costo posto: "))
            
            posto = PostoStandard(numero, fila, costo)
            teatro.aggiungi_posto(posto)
            
        case _:
            print("Tipo non valido!")

def prenota_posto_input(teatro):
    print("\n--- PRENOTA POSTO ---")
    numero = int(input("Numero posto: "))
    fila = input("Fila posto: ").upper()
    
    teatro.prenota_posto(numero, fila)

def libera_posto_input(teatro):
    print("\n--- LIBERA POSTO ---")
    numero = int(input("Numero posto: "))
    fila = input("Fila posto: ").upper()
    
    teatro.libera_posto(numero, fila)

if __name__ == "__main__":
    main()