
class Registro: 
    def __init__(self, elenco={}):
        self.elenco={}
    
    def modifica_registro(self):
        print("Modifica dei voti. . . ")
        counter = int(input("Quanti studenti modificare: "))
        for i in range (counter):
            nome = input("Inserisci nome: ")
            cognome = input("Inserisci cognome: ")
            voto = int(input("Inserisci il voto: "))
            self.elenco[(nome, cognome)] = voto
        print ("Hai inserito " + str(counter) +  " studenti")
       
    def visualizza_registro(self):
        print("Registro corrente")
        print(self.elenco) 
    
    def switch_ingresso(self):
        flag_ingresso = False
        while not flag_ingresso:
            print ("Benvenuto nel registro elettronico")
            print (" 1. Entra \n 2. Esci")
            scelta = int(input("Opzione scelta: "))
            if scelta == 1:
                self.switch_operazioni()
            elif scelta == 2:
                print("Uscita")
                break
            else:
                print("ATTENZIONE!!! Opzione non valida")
    
    def switch_operazioni(self):
        flag_op = False
        while not flag_op:
            print("Operazini disponibili")
            print (" 1. Inserisci studente/voto \n 2. Visualizza registro \n 3. Torna indietro")
            scelta = int(input("Opzione scelta: "))
            if scelta == 1:
                self.modifica_registro()
            elif scelta == 2:
                self.visualizza_registro()
            elif scelta == 3:
                print("Torna indietro\n")
                break
            else:
                print("ATTENZIONE!!! Opzione non valida")

class Alunno(Registro):
    def __init__(self, nome, voto, elenco={}):
        super().__init__(elenco)
        self.nomi = nome
        self.voto = voto
    
    
        
    
    
    
registro = Registro()
registro.switch_ingresso()


    
    