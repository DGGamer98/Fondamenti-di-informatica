'''Scrivere un programma che accede a un indice di una lista e gestisce l'eccezione se l'indice è fuori dai limiti della lista.'''

listaNumeri = [10, 4, 3, 1]

try:
    print(listaNumeri[5]) #Da errore -> 5 è un indice al di fuori
except IndexError:
    print("L'indice è al di fuori della lista")