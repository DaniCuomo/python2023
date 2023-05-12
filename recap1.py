''' Scrivi un programma che richieda all'utente di 
inserire una stringa e che conti quante volte ogni lettera appare nella stringa. '''

#INSERIRE UNA STRINGA DA TASTIERA 
stringa = input("Inserisci una parola: ")
print ('Hai inserito',stringa)

diz={}

for l in stringa:
    if l not in diz:    #diz esiste e non contiene niente, quindi le p in parole vengono copiate in dizionario
        diz[l]=1        #la p viene presa e messa nel dizionario
    else:
        diz[l]+=1       #se la parola già è presente in diz, contala una volta in più, per tutte le parole della lista 
print(diz)
    

 