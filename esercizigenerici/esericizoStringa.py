'''
Analisi di una stringa
Scrivi una funzione che riceve una stringa e stampa:

Quante lettere contiene
Quanti numeri contiene
Quanti caratteri speciali contiene (tutto il resto)
La stringa invertita
Quante volte appare la lettera più frequente
'''

s = "Hello123!@#World456"

def analisi_stringa(s):
    Lettere = 0
    Numeri = 0
    Speciali = sum(not c.isalnum() for c in s)
    lettere_frequenti = 0
    for x in s:
        if x.isalpha():
            Lettere+=1
        elif x.isdigit():
            Numeri+=1
    
    Invertita = s[::-1]
    #stringa_invertita = "".join(reversed(s))

    Lettera = input("conteggio lettera: ")
    #controllo lettere frequenti
    for x in s:
        if Lettera == x:
            lettere_frequenti+=1
    

    print(f"Lettere: {Lettere}")
    print(f"Numeri: {Numeri}")
    print(f"Speciali: {Speciali}")
    print(f"Invertita: {Invertita}")
    print(f"La lettera {Lettera} sta {lettere_frequenti} volte nella stringa")    
    

analisi_stringa(s)

#output atteso
'''
Lettere: 10
Numeri: 6
Speciali: 3
Invertita: 654dlroW#@!321olleH
Lettera più frequente: l (3 volte)
'''