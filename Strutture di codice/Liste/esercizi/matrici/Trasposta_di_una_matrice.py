'''
Obiettivo: costruire la trasposta di una matrice senza usare librerie come numpy.

Consegna:

Crea una matrice 3×3.
Genera una nuova matrice che rappresenti la trasposta (righe e colonne scambiate).
Stampa sia la matrice originale sia quella trasposta.
''' 


matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrice_trasposta = []

for j in range(len(matrice[0])): #capire il numero di colonne
    n = []
    for i in range(len(matrice)): #Capire il numero di righe
        n.append(matrice[i][j])

    matrice_trasposta.append(n)

for riga in matrice_trasposta:
    print(riga)


