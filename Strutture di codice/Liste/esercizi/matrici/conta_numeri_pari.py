matrice = [
    [4, 7, 10],
    [3, 8, 15],
    [6, 1, 12]
]

numeri_pari = []
numeri_pari1 = []

#prima opzione
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        valore = matrice[i][j]

        if valore%2 == 0:
            numeri_pari.append(valore)
            
print(numeri_pari)


#seconda opzione
for i in matrice:
    for j in i:
        if j%2 == 0:
            numeri_pari1.append(j)

print(numeri_pari1)

