matrice =  [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

trasposta_matrice = []

def trasposta(matrice):
    for j in range(len(matrice[0])):
        n = []
        for i in range(len(matrice)):
            n.append(matrice[i][j])
            
        trasposta_matrice.append(n)
        
    for i in trasposta_matrice:
        print(i) 
        
def somma_colonna(matrice, colonna):
    for j in range(len(matrice[0])):
        somma = 0
        for i in range(len(matrice)):
            somma+=matrice[i][colonna]
    
    return somma
    

trasposta(matrice)
print(somma_colonna(matrice, 0))