'''Scrivi una funzione che prende una stringa e restituisce la stringa invertita.'''

stringa = "Ciao mondo"

def inverti_String(stringa):
    inversa = ''
    indice = len(stringa) -1
    while indice >= 0:
        inversa += stringa[indice]
        indice -=1
    return inversa

print(inverti_String(stringa))