
#calcolatrice 
class Calcolatrice: 
    operazioni = [] #per memorizzare le operazioni
    numero_iterazioni = 0
    
    #per svuotare la lista delle operazioni
    def pulisci_operazioni(self):
        self.operazioni = []
        self.numero_iterazioni = o
    
    #per stampare lo storico risultato | operatore
    def carica_risultato (self, risultato, operatore):
        self.operazioni.append((risultato, operatore))
        return
    
    #operazioni
    def somma(self, valore1, valore2):
            return valore1+valore2
    def sottrai(self, valore1, valore2):
            return valore1-valore2         
    def moltiplica(self, valore1, valore2):
            return valore1*valore2
    
    #somma di tutti i risultati delle 3 operazioni scelte
    def totale(self):
        if self.operazioni == []:
            return None #NON STAMPARE NIENTE SE NON HAI FATTO NIENTE
        else:
            return self.operazioni[0][0] + self.operazioni[1][0] + self.operazioni[2][0]  
    
    def stampa_operazioni(self):
        if self.operazioni == []:
            print("Non sono state eseguite operazioni")
        else:
            for risultato, operatore in self.operazioni:
                print(f"Risultato: {risultato} | Operazione: {operatore}")
        return   

calcolatrice = Calcolatrice 

print ("BENVENUTO, SCELGI COSA VUOI FARE:\n") 
flag_ingresso = False

while not flag_ingresso: 
    scelta = int(input(" Premi 1 per CONTARE\n Premi 2 per STAMPARE\n Premi 3 per USCIRE: "))

    if scelta == 3:
        print("Sei uscito")
        flag_ingresso = True
    
    elif scelta == 1:
        calcolatrice.pulisci_operazioni()
        #op_flag non serve perché già conto con il while
        counter = 0
        while counter<3:
            operatore = input("scegli quale operatore vuoi fare (+  *  -)    ")
            
            if operatore == "+":
                    print ("hai scelto la somma")
                    valore1 = int(input("inserisci il primo valore: "))
                    valore2 = int(input("inserisci il secondo valore valore: "))    
                    risultato = calcolatrice.somma(valore1, valore2)
                    calcolatrice.carica_risultato(risultato, operatore)
                      
            elif operatore == "-":
                    print ("hai scelto la differenza\n")
                    valore1 = int(input("inserisci il primo valore: "))
                    valore2 = int(input("inserisci il secondo valore valore: "))
                    risultato = calcolatrice.sottrai(valore1, valore2)
                    calcolatrice.carica_risultato(risultato, operatore) 
                       
            elif operatore == "*":
                    print ("hai scelto la moltiplicazione\n")
                    valore1 = int(input("inserisci il primo valore: "))
                    valore2 = int(input("inserisci il secondo valore valore: "))
                    risultato = calcolatrice.moltiplica(valore1, valore2)
                    calcolatrice.carica_risultato(risultato, operatore)
            
            else:
                print("Operazione non consentita")  
        
        print("Somma totale risultati:",calcolatrice.totale())        
        
    elif scelta == 2:
        calcolatrice.stampa_operazioni() #stampo i risultati parziali
    
    else:
        print("scelta non valida")