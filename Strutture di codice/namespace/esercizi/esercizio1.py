# ESERCIZIO — LEGB con liste e dizionari

dati = {"nome": "Mario", "punti": 0}

def aggiorna_punti(valore):
    dati["punti"] +=valore
    return aggiorna_punti

def resetta_dati():
    global dati  
    dati = {"nome": "Reset", "punti": 0}

aggiorna_punti(10)
aggiorna_punti(5)
print(dati)  # → {"nome": "Mario", "punti": 15}

resetta_dati()
print(dati)  # → {"nome": "Reset", "punti": 0}


# DOMANDA TEORICA:
# Perché aggiorna_punti NON ha bisogno di "global" 
# ma resetta_dati SI?
# Scrivi la risposta come commento nel codice!

'''Perché nella funzione aggiorna_punti noi stiamo accedendo ad una key del nostro dizionario globale
Mentre resetta_dati sta creando un nuovo dizionario locale con lo stesso nome della globale. 
Quindi per renderlo globale dobbiamo usare global'''