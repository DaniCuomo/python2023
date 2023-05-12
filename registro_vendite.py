
print("Registro vendite")

print("Cosa vuoi fare:")
nome = ["prodotto_1", "prodotto_2", "prodotto_3"]
prezzo = [1.00 , 2.00 , 3.00]
codice = ['001', '002', '003']


dati = [nome, codice, prezzo]
articoli = {"dati":dati}


flag = False
while not flag: 
    comando = int(input("Premi 1 per aggiungere un articolo\n"
                    "Premi 2 per visualizzare il totale: "))

#inserimento nuova transazione (nome + prezzo + codice)
    if comando == 1:
        nuovo_nome = input("Inserire nome articolo: ")
        
        for n in nome:  
            if nuovo_nome not in nome:
                nome.append(nuovo_nome)    
            
            
        nuovo_codice = input("Inserire codice articolo: ")
        codice.append(nuovo_codice)    
        
        nuovo_prezzo = float(input("Inserire prezzo articolo: "))
        prezzo.append(nuovo_prezzo)    
        print (articoli)


    #somma del fatturato 
    elif comando == 2: 
        fatturato = 0.0
        for p in prezzo:
            fatturato = fatturato + p
        print("il fatturato totale ammonta a:", fatturato)
    
    altro = input("vuoi fare altro: Y/N . . . ")
    if altro == 'Y':
        flag = False
    else:
        flag = True   
