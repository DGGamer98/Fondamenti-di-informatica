'''Crea una tupla contenente tutti i numeri dispari compresi tra 1 e 20.'''
    
intTuple = tuple(x for x in range(0, 21) if x%2 == 1)
print(intTuple)
