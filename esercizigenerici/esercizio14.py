immagine = [
    [200,  50, 180,  30],
    [ 90, 170,  20, 210],
    [255,  80, 140,  60],
    [ 40, 190, 100, 220]
]

def stampa_immagine(immagine):
    for valore in immagine:
        print(*valore)

def negativo(immagine, valore):
    for i in range(len(immagine)):
        for j in range(len(immagine[0])):
            immagine[i][j]-=valore
    return immagine

def pixel_più_luminoso(immagine):
    pixel_luminoso = immagine[0][0]
    pos_x = 0
    pos_y = 0
    for i in range(len(immagine)):
        for j in range(len(immagine[i])):
            valore = immagine[i][j]
            if valore > pixel_luminoso:
               pixel_luminoso = valore
               pos_x = i
               pos_y = j
    return f"Il pixel più luminoso è {pixel_luminoso} in riga {pos_x} e colonna {pos_y}"
                

#stampa_immagine(immagine)
#print(negativo(immagine, 30))
print(pixel_più_luminoso(immagine))