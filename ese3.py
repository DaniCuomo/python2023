

#SCRIVERE UNA CALCOLATRICE ACCEDENDO DA UN MENU

flag_uscita = False #flag inizializzata a False
numero_1 = 0.0
numero_2 = 0.0

while not flag_uscita: #finché è vera la flag
    print("\nBenvenuto nel menu di scelta")
    print("PER ACCEDERE PREMI 1 ")
    print("PER USCIRE PREMI 0 ")
    scelta = int(input("SCELGI: . . . "))
    
    if scelta == 0:
        print("Sei uscito")
        flag_uscita=True #quando è True (diversa quindi dalla condizione del While) esci
         
    elif scelta == 1:
        #flag_uscita=False
        
        flag_accesso = False
        while not flag_accesso: #finché è vera la flag...
            print("\nBENVENUTO IN CALCOLATRICE")
            #TORNARE AL MENU PRINCIPALE
            indietro = input("Premi 9 per tornare indietro, altrimenti digita 'Avanti' . . .  ")
            if indietro == "9":
                flag_accesso = True
            elif indietro == "Avanti":
                flag_accesso = False
                
                operazione = input("\nScegli quale operazione  effettuare: +  -  *  / :  ")
                print("Inserisci i due numeri: ")
                numero_1= float(input("Primo numero: "))
                numero_2= float(input("Secondo numero: "))
                
                if operazione == '+':
                    print("hai scelto la somma")
                    somma = numero_1 + numero_2
                    print("La somma vale",somma)
                elif operazione == '-':
                    print("hai scelto la differenza")
                    differenza = numero_1 - numero_2
                    print("La differenza vale", differenza)
                elif operazione == '*':
                    print("hai scelto il prodotto")
                    prodotto = numero_1 * numero_2
                    print("Il prodotto vale", prodotto)
                elif operazione == '/':
                    print("hai scelto il rapporto")
                    rapporto = numero_1 / numero_2
                    print("Il rapporto vale", rapporto)
            else:
                print("Inserisci uno dei valori consentiti (9 / Avanti)")
           
            flag_uscita = False
            exit()

    '''ritorno = input("Vuoi fare altro? Y/N")
    
    if ritorno == 'Y':
        flag_accesso = True
    if ritorno == 'N':
        flag_accesso = True'''


       



    
    
    