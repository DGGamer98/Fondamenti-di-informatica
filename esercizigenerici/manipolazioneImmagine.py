immagine = [
    [200,  50, 180,  30],
    [ 90, 170,  20, 210],
    [255,  80, 140,  60],
    [ 40, 190, 100, 220]
]

immagineNegativa = []

def stampa_immagine(immagine):
    for pixel in immagine:
        print(*pixel)

def immagine_negativa(immagine):
    for x in range(len(immagine)):
        for y in range(len(immagine[x])):
            immagineNegativa.append(immagine[x][y]-255)

    # for y in immagine:
    #     for x in y:
    #         immagineNegativa.append(x-255)

def pixel_più_luminoso(immagine):
    pixel_luminoso = immagine[0][0]
    pos_x = 0
    pos_y = 0

    for x in range(len(immagine)):
        for y in range(len(immagine[x])):
            valore = immagine[x][y]
            if valore >= pixel_luminoso:
                pixel_luminoso = valore
                pos_x = x
                pos_y = y
    return f"Il pixel più luminoso: {pixel_luminoso} in posizione {pos_y}, {pos_x}"

def schiarisci (immagine, quantita):
    for x in range(len(immagine)):
        for y in range(len(immagine[x]))


#stampa_immagine(immagine)
# immagine_negativa(immagine)
# print(immagineNegativa)
print(pixel_più_luminoso(immagine))