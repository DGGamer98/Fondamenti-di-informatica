import math

def dividi(a, b):
    try:
        dividendo = int(a) / int(b)
    except ZeroDivisionError:
        print("Non si può dividere per 0")
    except ValueError :
        print("Le variabili devono essere degli interi")
    else:
        return dividendo
    

def radice_quadrata(numero):
    try:
        radice = math.sqrt(numero)
    except ValueError:
        print("Non può essere minore di 0")
    else:
        return radice
    
def accedi_lista(lista, indice):
    try:
        index = lista[indice]
    except IndexError:
        print("sei fuori dalla matrice")
    else:
        return index
    
# testa le funzioni così:
print(dividi(10, 2))      # → 5.0
print(dividi(10, 0))      # → gestisci errore
print(radice_quadrata(9)) # → 3.0
print(radice_quadrata(-4))# → gestisci errore

numeri = [1, 2, 3]
print(accedi_lista(numeri, 1))   # → 2
print(accedi_lista(numeri, 99))  # → gestisci errore