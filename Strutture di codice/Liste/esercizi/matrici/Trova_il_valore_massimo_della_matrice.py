matrice = [
    [12, 5, 7],
    [3, 20, 8],
    [15, 1, 10]
]

massimo = 0

for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        valore = matrice[i][j]

        if valore > massimo:
            massimo = valore

print("Il valore massimo è:", massimo)