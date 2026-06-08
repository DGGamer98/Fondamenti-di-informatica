'''Data la lista [3, 7, 2, 9, 5], crea una tupla contenente il triplo di ogni numero'''

numeri_lista = [3, 7, 2, 9, 5]

numeri_tupla = tuple(x*3 for x in numeri_lista)

print(numeri_lista)