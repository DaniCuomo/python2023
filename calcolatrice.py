

class Calcolatrice:
    operazioni = [] # lista per la memorizzazione di tutte le operazioni in forma (risultato, operatore)

    # metodo che svuota la lista di operazioni
    def pulisci_operazioni(self):
        self.operazioni = []

    # metodo che carica all'interno della lista operazioni il risultato parziale e l'operatore che lo ha generato
    def carica_risultato (self, risultato, operatore):
        self.operazioni.append((risultato, operatore))
        return

    def somma(self, primo_numero, secondo_numero): 
        return primo_numero + secondo_numero
    
    def sottrai(self, primo_numero, secondo_numero): 
        return primo_numero - secondo_numero
    
    def moltiplica(self, primo_numero, secondo_numero): 
        return primo_numero * secondo_numero
    
    # metodo per il calcolo del risultato della somma di tutti i risultati parziali calcolati
    def totale(self):
        if self.operazioni == []:
            return None #NON STAMPARE NIENTE SE NON HAI FATTO NIENTE
        else:
            return self.operazioni[0][0] + self.operazioni[1][0] + self.operazioni[2][0]
    
    # metodo per stampare i risultati parziali con l'operatore di riferimento
    def stampa_operazioni(self):
        if self.operazioni == []:
            print("Non sono state eseguite operazioni")
        else:
            for risultato, operatore in self.operazioni:
                print(f"Risultato: {risultato} | Operazione: {operatore}")
        return
    

exit_flag = False
calcolatrice = Calcolatrice() 

while not exit_flag: #fintato che . . . 
    print("\nSelezionare l'opzione desiderata")
    print("1. Conta")
    print("2. Stampa")
    print("0. Esci")
    
    scelta = input("Scegli: ")

    if scelta == '0':
        # uscita dal programma
        print("Sei uscito")
        exit_flag = True

    elif scelta == '1':
        calcolatrice.pulisci_operazioni() # svuoto la lista di operazioni per memorizzare le nuove operazioni
        contatore = 0 # CONTA LE OPERAZIONI

        while contatore < 3:
            #contatore += 1
            #print(f"- operazione numero {contatore} -")
            operatore = input("Inserire l'operatore (+, -, *): ")
            primo_numero = float(input("Inserire il primo numero: "))
            secondo_numero = float(input("Inserire il secondo numero: "))
            
            if operatore == '+':
                risultato = calcolatrice.somma(primo_numero, secondo_numero)
                calcolatrice.carica_risultato(risultato, operatore)

            elif operatore == '-':
                risultato = calcolatrice.sottrai(primo_numero, secondo_numero)
                calcolatrice.carica_risultato(risultato, operatore)

            elif operatore == '*':
                risultato = calcolatrice.moltiplica(primo_numero, secondo_numero)
                calcolatrice.carica_risultato(risultato, operatore)

            else:
                print("Errore, l'operatore da te selezionato non esiste")
                contatore -= 1 # non conto questa iterazione in quanto non ha restituito un'operazione valida
            
            print()
        
        print(f"\nSomma totale: {calcolatrice.totale()}") #restituisco la somma totale delle operazioni

    elif scelta == '2':
        calcolatrice.stampa_operazioni() #stampo i risultati parziali

    else:
        print("Errore, l'opzione da te selezionata non esiste")