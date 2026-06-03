'''Scrivere un programma che chiede all'utente di inserire un numero, convertendolo in intero, e usa `finally` per confermare l'input ricevuto.'''

numero = input("> ")

try:
    numero_convertito = int(numero)
    print(numero_convertito)

except NameError as e:
    print("nome non definito")
except ValueError as e:
    print(e)
finally:
    print("Fine")