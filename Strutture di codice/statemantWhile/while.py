x = 0
while x < 3: #finchè il valore di x è minore di 3, esegui la site
    print(x)
    x += 1 #ogni iterazione aumento di 1
    
#Loop infinito(controllato)
while True:
    x = input("Inserire una stringa: ")
    if x == 'stop':
        break #per uscire un loop infinito
    print(x)
    
while True:
    x = input("Inserire una stringa: ")
    if x == 'stop':
        break # per uscire un loop infinito
    if x < 'b':
        continue # ritorna ad eseguire il loop, interrompendo l'iterazione
    print(x) 
    