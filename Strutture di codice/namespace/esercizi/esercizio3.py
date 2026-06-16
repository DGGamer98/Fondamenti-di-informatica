# ESERCIZIO — LEGB con classi e funzioni annidate

contatore_globale = 100

class Magazzino:
    contatore_globale = 0  # attributo di classe, stesso nome della variabile globale!
    
    def __init__(self, nome):
        self.nome = nome
        Magazzino.contatore_globale += 1
    
    def mostra_contatori(self):
        # quale contatore_globale vedi qui dentro? --> contatore_globale = 1
        # quello della classe Magazzino o quello -? --> globale
        # stampa entrambi usando i prefissi corretti
        print(contatore_globale)
        print(Magazzino.contatore_globale)

magazzino = Magazzino("test")
magazzino.mostra_contatori()

# ESERCIZIO 2 — closure con enclosing
def crea_moltiplicatore(fattore):
    def moltiplica(numero):
        # questa funzione interna usa "fattore"
        # fattore è Local, Enclosing, Global o Built-in per moltiplica? --> Enclosing
        nonlocal fattore
        return numero * fattore
    return moltiplica

doppio = crea_moltiplicatore(2)
triplo = crea_moltiplicatore(3)

print(doppio(5))   # → 10 
print(triplo(5))   # → 15
# Perché doppio e triplo si "ricordano" valori diversi di fattore
# # anche se crea_moltiplicatore è già finita?


# ESERCIZIO 3 — il classico errore
totale = 0

lista_numeri =  [3, 2, 4, 6]

#soluzione 1
def somma_lista(numeri):
    #soluzione 1
    global totale
    for n in numeri:
        totale += n  # ❌ questo codice lancia un errore!
    return totale

#soluzione 2
def somma_lista1(numeri):
    totale = 0
    for n in numeri:
        totale += n  
    return totale

# Perché questo codice lancia UnboundLocalError?
# Come lo correggi in DUE modi diversi?
# (suggerimento: uno dei due modi NON usa global)

addizione = somma_lista(lista_numeri)
print(totale)

somma = somma_lista1(lista_numeri)
totale = somma
print(totale)