'''Con "as e" puoi accedere al messaggio dell'eccezione e stamparlo o usarlo nel codice.'''

try:
    risultato = 10/4
except ZeroDivisionError as e: #Imposto un alisa a ZeroDivisionError e lo stampo
    print(f"Messaggio di errore {e}")
else:
    print("Tutto ok")
    print(risultato)
finally:
    print("Fine codice")


'''Proviamo l'utilizzo anche con una lista'''
try:
    lista = [10,4,2]
    print(lista[10]) #proviamo ad accedere alla posizione di una lista inesistente
except IndexError as e: 
    print(f"Errore {e}")
