# def somma (a, b):
#     totSomma = a + b
#     return totSomma


try:
    a = 10
    b = 10
    print(somma(a,b))
except NameError as e:
    print("La funzione non esiste")
finally:
    print("Fine funzione")


try:
    oggetto = {}
    oggetto.metodo_inesisente()
except AttributeError:
    print("Metodo inesistente")