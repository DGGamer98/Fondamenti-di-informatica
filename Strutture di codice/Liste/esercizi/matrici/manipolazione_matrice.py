matrice = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrice_trasposta = []
matrice_righe_invertite = matrice[::-1]
matrice_colonne_invertite = [riga[::-1] for riga in matrice]

def stampa_matrice(matrice):
    for x in matrice:
        print(*x)


def trasposta(matrice):
    for j in range(len(matrice[0])):
        n=[]
        for i in range(len(matrice)):
            n.append(matrice[i][j])
        matrice_trasposta.append(n)

    print("x---------------------")

    for x in matrice_trasposta:
        print(*x)


def inverti_righe(matrice):
    for x in matrice_righe_invertite:
        print(*x)

def inverti_colonne(matrice):
    for x in matrice_colonne_invertite:
        print(*x)


stampa_matrice(matrice)
trasposta(matrice)
inverti_righe(matrice)
inverti_colonne(matrice)