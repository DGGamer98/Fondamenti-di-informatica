'''Scrivere un programma che tenta di dividere 10 per un numero inserito dall'utente, gestendo l'errore se l'utente inserisce 0.
'''

try:
    numero = int(input("> "))
    totale = 10 / numero
    print(totale)
except ZeroDivisionError:
    print("Non si può dividere per 0")