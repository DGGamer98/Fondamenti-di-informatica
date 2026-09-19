matrice = [
    [2,5,8,3],
    [9,1,6,4],
    [7,3,2,8],
    [4,6,1,5]
]


def somma_diagonale(matrice):
    diagonale = []
    somma = 0

    for i in range(len(matrice)):
            diagonale.append(matrice[i][i])


    print(diagonale)

    for x in diagonale:
         somma+=x

    return f"somma della diagonale é {somma}"


def riga_con_somma_massima(matrice):

    lista_somme = []
    for i in range(len(matrice)):
        somma_riga = 0
        for j in range(len(matrice[0])):
            somma_riga+=matrice[i][j]
        lista_somme.append(somma_riga)

    print(lista_somme)

def trasposta(matrice):
    trasposta = []
    for j in range(len(matrice[0])):
        n=[]
        for i in range(len(matrice)):
            n.append(matrice[i][j])
        trasposta.append(n)
        
    return trasposta




print("=== somma diagonale principale della matrice")
print(somma_diagonale(matrice))

print("=== riga con somma massina ===")
print(riga_con_somma_massima(matrice))

print("=== trasposta ===")
print(trasposta(matrice))