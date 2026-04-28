'''Creare un programma che continua a far inserire all'utente dei numeri interi,
   il programma si ferma quando vengono inseriti più numeri negativi di quelli positivi'''

numNegativi = []
numPositivi = []

tot_numeriNegativi = 3

while True:
    x = int(input("Inserisci dei numeri: "))
    if x > 0:
        numPositivi.append(x)
        print(f"Numero {x} aggiunto")
    if x < 0:
        numNegativi.append(x)
        print(f"Numero {x} aggiunto")
        #regola numeri negativi consentiti 3
        if len(numNegativi) == 3:
            break
    elif x == 0:
        break
    
print(numNegativi)
print(numPositivi)