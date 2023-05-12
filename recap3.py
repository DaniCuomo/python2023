'''Scrivere un programma che prenda una lista di numeri come input e 
rimuove i duplicati dalla lista, lasciando solo i valori "unici". 
L'ordine degli elementi nella lista deve rimanere invariato '''


#lista = input("Inserire valori da controllare: ")
#list(lista)
#print (set(lista))

'''
n_set = {1, 2, 3, 5, 6, 6, 8}
print(n_set)

numeri = input("Inserisci i numeri: ").replace(" ","")
print(set(numeri)) 

'''
numeri=input("Inserisci i numeri da controllare: ").replace(" ","")
numeri_check=[]

for el in numeri:
    if el not in numeri_check:
        numeri_check.append(el)

print(numeri_check)