'''Scrivere un programma che chiede all'utente di inserire un numero e divide 100 per quel numero, 
   stampando un messaggio in un blocco `finally`.'''

divisore = int(input("> "))

try:
    risultato = 100/divisore
    print(risultato)
except ZeroDivisionError as e:
    print("Non si può fare una divisione per 0")
except ValueError as e:
    print("Il valore non è valido")
finally:
    print("Fine dell'eccezione")