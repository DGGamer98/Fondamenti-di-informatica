'''Scrivere un programma che chiede all'utente di inserire un valore e tenta di usarlo come indice per una lista vuota,
   gestendo l'errore.'''

myList = [2,5,8,1]

try:
    insert_index = int(input("Inserisci l'indicie"))
    print(myList[insert_index])
except IndexError as e:
    print("L'indice è fuori dalla lista", e)