'''Scrivere un programma che converte una stringa in un numero intero e gestisce l'eccezione se la stringa non è un numero valido.'''

def somma (a, b):
    try:
        totale = int(a) + int(b)
        print (totale)
    except ValueError:
        print("Formato delle variabili non valido")
     
             
#somma("20",20)   
somma("venti",20) 