from random import shuffle

def numeri_casuali(n):
    numeri = []
    for i in range(1, 9 + 1):
        numeri.append(i)
    shuffle(numeri) #mescola i valori della matrice
    return numeri

def matrice_quadrata(numeri, n):
    matrice = []
    for riga in range(n):
        numeri_riga = []
        for col in range(n):
            index = riga*n + col
            numeri_riga.append(numeri[index])
        matrice.append(numeri_riga)
    return matrice

def print_matrice(matrice,n):
    for i in range(n):
        for j in range(n):
            print(matrice[i][j], end="\t")
        print()
        
numeri = numeri_casuali(9)
print(numeri)

matrice = matrice_quadrata(numeri, 3)
print(matrice)