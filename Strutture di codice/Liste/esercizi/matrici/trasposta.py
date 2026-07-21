matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonale =  []
trasposta_matrix = []

def diagonale_principale(matrice):
    for i in range(len(matrice)):
        diagonale.append(matrice[i][i])

    for i in diagonale:
        print(i)

def trasposta (matrice):
    for j in range(len(matrice[0])):
        n=[]
        for i in range(len(matrice)):
            n.append(matrice[i][j])
    
        trasposta_matrix.append(n)

    for x in trasposta_matrix:
        print(x)

def somma_colonna(matrice, colonna):
    somma = 0
    for i in range(len(matrice)):
        somma+=matrice[i][colonna]
    
    print(f"somma colonna {colonna} è {somma}")


diagonale_principale(matrice)
trasposta(matrice)
somma_colonna(matrice, 1)