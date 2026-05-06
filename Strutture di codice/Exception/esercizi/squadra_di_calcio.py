'''TODO Davide
def aggiungi_giocatore(squadra, nome):
    # gestisci ValueError se nome è una stringa vuota ""
    # se il giocatore è già presente stampa "Giocatore già in squadra!"
    # altrimenti aggiunge il nome alla lista

def rimuovi_giocatore(squadra, indice):
    # gestisci IndexError se l'indice non esiste
    # altrimenti rimuove il giocatore con pop(indice)
    # stampa chi è stato rimosso

def cerca_giocatore(squadra, nome):
    # gestisci ValueError se nome non è nella lista
    # usa lista.index(nome) → lancia ValueError se non trovato
    # restituisce l'indice dove si trova il giocatore

def mostra_squadra(squadra):
    # stampa tutti i giocatori con il loro indice
    # es. "0 → Ronaldo"
'''

def aggiungi_giocatore(squadra, nome):
    if nome in squadra:
        print("Giocatore già presente")
        return
    if nome == "":
        raise ValueError ("Nome non può essere una stringa vuota")
    else:
        squadra.append(nome)
        print("giocatore aggiunto")
    
        
def rimuovi_giocatore(squadra, indice):
    try:
        squadra[indice]
    except IndexError:
        print("Sei uscito fuori dalla lista")
    else:
        squadra.pop(indice)
        print("Giocatore rimosso")
        
def cerca_giocatore(squadra, nome):
    try:
        squadra.index(nome)
    except ValueError:
        print("giocatore non trovato")
    else:
        return squadra.index(nome)
    
def mostra_squadra(squadra):
    counter = 0
    for x in squadra:
        counter+=1
        print(f"{counter} -> {x}")
        
        
        
squadra = []

# aggiungi giocatori
aggiungi_giocatore(squadra, "Ronaldo")
aggiungi_giocatore(squadra, "Messi")
aggiungi_giocatore(squadra, "Mbappé")
#aggiungi_giocatore(squadra, "")
#aggiungi_giocatore(squadra, "Messi")


#rimuovi_giocatore(squadra, 99)
print(cerca_giocatore(squadra, "Messi"))

mostra_squadra(squadra)

        
