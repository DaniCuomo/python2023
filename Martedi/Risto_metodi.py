
#MENU RISTORANTE
menu = ["Antipasto", 10, "Primo", 20, "Secondo", 30, "Dolce", 40]
piatto_scelto = []

def ordina():
    print("Menu disponibile. . . \n")
    print (menu)
    
    flag_comanda=False
    while not flag_comanda: 
        piatto=input("\nCosa vuoi mangiare?   ")
        if piatto not in menu:
            print ("PIATTO NON DISPONIBILE\n")
        else: 
            piatto_scelto[piatto]
            altro = input("vuoi qualcos'altro: Y/N . . . ")
            if altro == "Y":
                flag_comanda = False
            elif altro == "N":
                flag_comanda = True
                     
def modifica():
    print("Menu disponibile")
    print(menu)
    indice = int(input("Inserire l'indice del valore da modificare: "))
    nome_mod = input("Nuovo nome/prezzo: ")
    menu[indice] = nome_mod
    print("Menu modificato")
    print (menu)
        

def conto():
    nominativo = input("Inserire nominativo: ")
    print(piatto_scelto)

                       


flag_scelta = False

while not flag_scelta:
    print("SCELTA DELLE OPZIONI")
    scelta = int(input(" 1.ENTRARE\n 2.USCIRE\n"))
    if scelta == 2:
        print("Arrivederci")
        flag_scelta = True
    elif scelta == 1:
        flag_comanda = False
        print("Benvenuto nel ristorante")
        print("SCELTA DELLE OPZIONI")
        print(" 1. ORDINARE\n 2. MODIFICARE\n 3. CHIEDERE IL CONTO ")
        opzione = int(input())
        if opzione == 1:
            ordina()
            
        elif opzione == 2:
            modifica()
            
        elif opzione == 3:
            conto()
        


