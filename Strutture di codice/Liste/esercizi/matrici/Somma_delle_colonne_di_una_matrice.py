matrice = [
    [2,4,6],
    [1,3,5],
    [7,8,9]
]

for j in range(len(matrice[0])):
    somma = 0
    for i in range(len(matrice)):
        somma+=matrice[i][j]

    print(somma)