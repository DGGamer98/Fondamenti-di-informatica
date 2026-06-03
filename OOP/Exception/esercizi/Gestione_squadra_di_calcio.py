import math

def dividi(a, b):
    try:
        dividendo = int(a) / int(b)
    except ZeroDivisionError:
        print("non si può dividere per 0")
    except ValueError:
        print("il formato delle variabili non è valido")
    else:
        return dividendo

def radice_quadrata(numero):
    try:
        radice = math.sqrt(numero)
    except ValueError:
        print("il numero è negativo")
    else:
        return radice
    
def accedi_lista(lista, indice):
    try:
        print(lista[indice])
    except IndexError:
        print("L'indice non esiste fuori dalla matrice")
    else:
        return lista[indice]




matrix = [10, 4, 8]

print(dividi(10, "a"))
print(radice_quadrata(-5))
print(accedi_lista(matrix, 1))