
#definisco una classe cliente
class Cliente:
    
    def __init__(self):
        self.nominativo = ""
        self.conto_cliente = {'ordini':{}, 'totale':0.00}



# flag avvio programma
flag_start = False

# inizializzare il menu e il conto
menu = {'Antipasto': 10.00, 'Primo': 20.00, 'Secondo': 25.00, 'Dessert': 5.00}
listaconti = []

# avvio programma
while not flag_start:
    
    # controllo user:
    print("Benvenuto, scegli cosa fare:")
    print(" 1. ENTRARE\n 2. USCIRE")
    scelta = input()
    
    if scelta == '1':
        flag_cliente = False
        while not flag_cliente:
            
            print("1. Comanda\n"
                "2. Aggiungi un piatto\n"
                "3. Rimuovi un piatto\n"
                "4. Chiedi il conto\n"
                "5. Altri conti")
            scelta_cliente = input()

            
            if scelta_cliente == '1':
                print("MENU DISPONIBILE:\n")
                
                for piatto, prezzo in menu.items():
                    print(f"{piatto} : €{prezzo}")
                print() 
                
                cliente = Cliente()
                
                cliente.nominativo = input("Inserisci il tuo nominativo: ")
                piatto = input("Inserisci il nome del piatto: ")
                #Check piatto nel menu, se si chiedimi la quantità
                if piatto in menu:
                    qta = int(input("Inserisci le qta: "))
                    if piatto not in cliente.conto_cliente['ordini']:
                        cliente.conto_cliente['ordini'] |= {piatto : qta}
                        cliente.conto_cliente['totale'] += menu[piatto] * qta
                    else:
                        gia_presente = cliente.conto_cliente['ordini'][piatto]
                        cliente.conto_cliente['ordini'] |= {piatto : gia_presente + qta}
                        cliente.conto_cliente['totale'] += menu[piatto] * qta
                else:
                    print("ATTENZIONE, PIATTO NON DISPONIBILE\n")
            
            #per aggiungere un nuovo piatto
            elif scelta_cliente == '2':
                piatto = input("Inserisci il piatto: ")
                prezzo = float(input("Inserisci il prezzo: "))
                menu[piatto] = prezzo
                print(f"Hai aggiunto il piatto {piatto} a € {prezzo} nel menu.")
            
            #per rimuovere un piatto già presente
            elif scelta_cliente == '3':
                piatto = input("Inserisci il piatto: ")
                del menu[piatto]
                print(f"Hai rimosso il piatto {piatto} a € {prezzo} dal menu.")
            
            #STAMPA DEL CONTO 
            elif scelta_cliente == '4':
                print("Conto: ")
                for piatto, qta in cliente.conto_cliente['ordini'].items():
                    print(f"{piatto} : {qta} pz")
                print("TOTALE : €", cliente.conto_cliente["totale"],"\n")
                listaconti.append(cliente)
                
                print("Arrivederci!")
                flag_cliente = True
            
            
            elif scelta_cliente == '5':
                print("Conti vari:\n")
                for cliente in listaconti:
                    print(f"{cliente.nominativo} : {cliente.conto_cliente['totale']}€")
            
            #scelta errata            
            else:
                print("SCELTA NON VALIDA.\n")
    
    #scelta uscita dal programma          
    elif scelta == '2':
        print("Arrivederci!")
        flag_start = True

    #scelta errata         
    else:
        print(" !!! SCELTA NON VALIDA !!! ")