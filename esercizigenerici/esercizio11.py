'''
Analisi parole
Scrivi una funzione che riceve una frase e:

Conta quante parole ci sono
Trova la parola più lunga
Conta quante parole iniziano con una lettera maiuscola
Restituisce la frase al contrario (parole invertite, non caratteri) 
'''

s = "Il Gatto dorme sul Divano ogni giorno"

def analizza_frase(s):
    newFrase = s.split()
    print(newFrase)

    parole = len(newFrase)

    for x in newFrase:
        if len(x) >= 6:
            print(f"Parola lunga: {x}")

    counter = 0
    paroleMaiuscole = []
    for y in newFrase:
        if y[0].isupper():
            counter+=1
            paroleMaiuscole.append(y)

    paroleString = " ".join(paroleMaiuscole)
    
    lista_invertita = newFrase[::-1]

    print(f"ci sono {counter} parole e sono {paroleString}")
    print(f"parole totale {parole}")
    print(f"lista invertita {lista_invertita}")
analizza_frase(s)