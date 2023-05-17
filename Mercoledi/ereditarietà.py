'''
class Persona: 
    
    # attributo già valorizzati
    tipo = "umano"
    
    # costruttore
    def __init__(self, Nome, Eta):
        self.Nome = Nome
        self.Eta = Eta
        
    # metodi
    def MasterD(self):
        print("Ciao sono " + self.Nome + ", ho " + str(self.Eta) + " e sono " + self.tipo)
        
X = Persona("Mirko", 99)
X.MasterD() 
'''

class Uno:
    
    uno = "UNO"
    
    def __init__(self, Nome):
        self.Nome = Nome
        
    def stampaUno(self):
        print("Ciao sono " + self.uno )
        

primo = Uno("Nonno")
primo.stampaUno()

class Due(Uno):
    def __init__(self, Nome):
        super().__init__(Nome)
    
    due = "DUE"
    
    def stampaDue(self):
         print("Ciao ero " + self.uno + " ora sono " + self.due )

secondo = Due("Papà")
secondo.stampaDue()

class Tre(Due):
    def __init__(self, Nome):
        super().__init__(Nome)
    
    tre = "TRE"
    
    def stampaTre(self):
        print ("Ciao, sono stato " + self.uno + " poi " + self.due + " ora sono " + self.tre)

terzo = Tre("Figlio")
terzo.stampaTre()