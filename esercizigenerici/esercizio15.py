immagine = [
    [100, 150, 200, 250],
    [ 50,  80, 120, 180],
    [200, 100,  60,  30],
    [ 10,  40,  90, 220]
]


def stampa_immagine_matrice(immagine):
    for i in immagine:
        print(*i)
           
def negativo(immagine):
    valore = int(input("valore: "))
    for i in range(len(immagine)):
        for j in range(len(immagine[i])):
           immagine[i][j]-=valore
    return immagine

def specchio_orizzontale(immagine):
    lista_inversa = []
    for i in immagine:
        inversione_pixel = i[::-1]
        lista_inversa.append(inversione_pixel)
    return lista_inversa

def specchio_verticale(immagine):
    righe_inverse = []
    for x in (immagine[::-1]):
        righe_inverse.append(x)
           
    return righe_inverse    
            
print("=== stampa pixel ===")
stampa_immagine_matrice(immagine)

print("=== stampa negativo ===")
print(negativo(immagine))

print("=== stampa orizzontale ===")
print(specchio_orizzontale(immagine))

print("=== specchio verticale ===")
print(specchio_verticale(immagine))