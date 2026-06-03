lista = ["pasta","arancia","fortnite","minecraft","arancione"]

def parole_con_lettera(lista, lettera):
    risultato = []
    for parola in lista:
        if parola[0] == lettera:
            risultato.append(parola)
    return risultato
        
print(parole_con_lettera(lista, lettera="a"))