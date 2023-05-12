
frase = input("Inserisci la frase di cui contare le parole occorse: \n")


parole = frase.split()
print("Frase splittata: ")
print(frase.split())

#definizione dizionario
diz={}

for p in parole:
    if p not in diz:
        diz[p] = 1
    else:
        diz[p] +=1

print ("\nLe occorrenze delle parole sono le seguenti\n",diz)