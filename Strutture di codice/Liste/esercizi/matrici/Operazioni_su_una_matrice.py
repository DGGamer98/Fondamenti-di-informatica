matrice = [
    [4,  8,  2, 6],   # riga 0
    [3,  7,  9, 1],   # riga 1
    [5,  2,  4, 8]    # riga 2
]

def somma(matrice):
    somma = 0 #Variabile d'appoggio
    for i in matrice:
        for j in i: # scorro gli indici di ogni lista annidata
            somma+=j
    return somma

def media_totale(matrice, somma): #associo la funzione
    counter = 0
    for i in matrice:
        for j in i:
            counter+=1 #Contiamo l'indice interno di ogni lista    
    media_matrice = somma / counter
    return media_matrice

def trova_valore_massimo(matrice):
    lista = [] #lista vuota
    for i in matrice:
        for j in i:
            lista.append(j) #sposto tutti gli elementi

    valoreMax = max(lista)
    return valoreMax

def somma_riga(matrice, y):
    somma = 0
    for i in matrice[y]: #già ho impostato l'indice a 0 con y usando l'accesso per indice
        somma+=i
    return somma
    

somma_matrice = somma(matrice)

print(f"somma matrice {somma(matrice)}")
print(f"Media della matrice {media_totale(matrice, somma_matrice)}")
print(f"Trova il valore massimo {trova_valore_massimo(matrice)}")
print(f"Somma la riga {somma_riga(matrice, 0)}")
