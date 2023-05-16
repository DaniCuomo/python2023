

class Piatto:
    nome = ""
    prezzo = 0.0

    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo
    
    def mod_nome(nome):
        nome = nome

    def mod_prezzo(prezzo):
        prezzo = prezzo

    def stampa(nome, prezzo):
        return f"Piatto: {nome} | Prezzo: € {prezzo}"


menu = [Piatto("Primo", 10.0), Piatto("Secondo", 20.0), Piatto("Terzo", 30.0), Piatto("Quarto", 40.0)]

print(Piatto)