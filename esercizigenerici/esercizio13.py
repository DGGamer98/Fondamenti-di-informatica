matrice = [
    [5,  3,  8,  1],
    [2,  9,  4,  7],
    [6,  1,  3,  8],
    [4,  7,  2,  5]
]


def somma_diagonale(matrice): #diagonale --> 5,9,3,5
    somma_diagonale = 0
    for i in range(len(matrice)):
        somma_diagonale+=matrice[i][i]
    return somma_diagonale
        

def routa_90(matrice):
    matrice_trasposta = []
    for j in range(len(matrice[0])):
        n=[]
        for i in range(len(matrice)):
            n.append(matrice[i][j])
        matrice_trasposta.append(n)
    
    for x in matrice_trasposta:
        print (x)

def cerca_elemento(matrice):
    valore = int(input("Inserisci il valore da cercare, solo numeri interi: "))
    pos_x = 0
    pos_y = 0
    for x in range(len(matrice)):
        for y in range(len(matrice[0])):   
            pos_x = x
            pos_y = y
            if valore == matrice[x][y]:
                return f"valore {valore} in riga x: {pos_x} colonna y: {pos_y}"
    return None


def sostituisci(matrice, vecchio, nuovo):
    for x in range(len(matrice)):
        for y in range(len(matrice[x])):
            if vecchio == matrice[x][y]:
                matrice[x][y] = nuovo
            else:
                continue
    
    for x in matrice:
        print(*x)
                
    

# print(somma_diagonale(matrice))
# print(routa_90(matrice))
# print(cerca_elemento(matrice))
sostituisci(matrice, 3, 10)

            
    