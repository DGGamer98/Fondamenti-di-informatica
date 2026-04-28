x = 0
while x < 3: #finche x è minore di 3 esegui
    print(x)
    x+=1 #aumenta una unità il valore di x
    
'''Loop infinito'''
while True:
    x = input("Inserire una stringa: ")
    if x == 'stop':
        break #interrompe immediatamente l'iterazione
    
    if x < "b": #non stampa x se la frase inizi con a
        continue # ritornare all'inizio dell'loop e ricominciare
    print(x)