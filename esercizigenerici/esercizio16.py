immagine = [
    [120,  80, 200,  40],
    [ 60, 180,  90, 150],
    [220,  30, 170,  70],
    [ 50, 210, 100, 190]
]


def stampa_immagine(immagine):
    for riga in immagine:
        print(*riga)
        
def ruota_90(immagine):
    trasposta = []
    for j in range(len(immagine[0])):
        n = []
        for i in range(len(immagine)):
            n.append(immagine[i][j])
        trasposta.append(n)
        
    for riga in trasposta[::-1]:
        trasposta.append(riga) #Sovrascrivo la lista trasposta(override)
    
    return trasposta 

def pixel_sopra_media(immagine):
    new_image = []
    counter = 0 #variabile contatore d'appoggio
    somma = 0
    for i in range(len(immagine)):
        for j in range(len(immagine[i])):
            #calcolo la media
            counter+=1
            somma+=immagine[i][j]
    media = somma/counter
    print(f"[LOG] media {media}")
    
    for i in range(len(immagine)):
        for j in range(len(immagine[i])):
            #confronto la media con i pixel
            if media < immagine[i][j]:
                immagine[i][j] = 0
                new_image.append(immagine[i][j])
            elif media >= immagine[i][j]:
                immagine[i][j] = 255
                new_image.append(immagine[i][j])
            
    return new_image
        
            
def specchio_e_negativo(immagine):
    immagine_negativa = []

    for riga in immagine:
        riga_specchiata = riga[::-1]
        immagine_negativa.append(riga_specchiata)
    return immagine_negativa
    

        
print("=== stampa immagine ===")
stampa_immagine(immagine)

print("=== matrice trasposta ===")
print(ruota_90(immagine))

print("=== pixel sopra la media ===")
print(pixel_sopra_media(immagine))

print("=== specchio negativo ===")
print(specchio_e_negativo(immagine))