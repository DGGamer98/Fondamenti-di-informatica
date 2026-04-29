'''TODO Davide
Esercizio 1 — Facile: Calcolatrice sicura
Scrivi una funzione per ognuna delle 4 operazioni aritmetiche. Ogni funzione deve gestire le eccezioni con try/except:
python

def addizione(a, b):
    # gestisci ValueError se a o b non sono numeri

def sottrazione(a, b):
    # gestisci ValueError se a o b non sono numeri

def moltiplicazione(a, b):
    # gestisci ValueError se a o b non sono numeri

def divisione(a, b):
    # gestisci ValueError se a o b non sono numeri
    # gestisci ZeroDivisionError se b è 0
Con un menu while che chiede i due numeri e chiama la funzione giusta. Se l'utente inserisce lettere invece di numeri, il programma non deve crashare ma stampare un messaggio di errore e riproporre il menu.
'''

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