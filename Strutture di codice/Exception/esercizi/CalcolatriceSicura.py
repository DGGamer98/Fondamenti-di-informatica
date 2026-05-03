def addizione(a, b):
    try:
        # Convertiamo forzatamente i valori
        risultato = int(a) + int(b)
        return risultato
    except ValueError:
        return "Errore: a o b non sono numeri validi."
    
def sottrazione(a, b):
    try:
        sottrazione = int(a) - int(b)
        return sottrazione
    except ValueError:
        return "Errore: a o b non sono numeri validi per la sottrazione"

def moltiplicazione(a ,b):
    try:
        risultato = int(a) * int(b)
        return risultato
    except ValueError:
        return "Errore: a o b non sono numeri validi per la moltiplicazione"
    
def divisione(a, b):
    try:
        risultato = int(a) / int(b)
        return risultato
    except ValueError:
        return "Errore: a o b non sono numeri validi per la divisione"
    except ZeroDivisionError as e:
        print(e)


#TODO Davide costruire un main per una finestra interattiva in console
print(addizione(20, "23"))    
print(addizione(20, "ciao"))  # Cattura il ValueError e stampa il messaggio

print(sottrazione(20,10))
print(sottrazione(30,"12")) 
print(sottrazione(20,"test"))


print(moltiplicazione(20, 20))
print(moltiplicazione(10, "3"))
print(moltiplicazione(12,"ciao"))

print(divisione(10, 0))
print(divisione(10, 3))
print(divisione(2, "cao"))