immagine = [
    [240, 30, 180, 60],
    [90, 200, 45, 210],
    [150, 75, 220, 20],
    [40, 190, 100, 160]
]

def negativo(immagine):
    for i in range(len(immagine)):
        for j in range(len(immagine[0])):
            immagine[i][j]-=255

    return immagine

def schiarisci(immagine, valore):
    for i in range(len(immagine)):
        for j in range(len(immagine[0])):
            immagine[i][j] += valore
            if immagine[i][j] > 255:
                immagine[i][j] = 255

    return immagine

def pixel_medi(immagine):
    new_image = []
    for i in range(len(immagine)):
        for j in range(len(immagine[0])):
            if immagine[i][j] in range(100, 200):
                new_image.append(immagine[i][j])
            elif immagine[i][j] < 100:
                immagine[i][j] = 0
                new_image.append(immagine[i][j])
            elif immagine[i][j] > 200:
                immagine[i][j] = 255
                new_image.append(immagine[i][j])

    return new_image


def specchio_verticale(immagine):
    righe_inverse = []

    for i in(immagine[::-1]):
        righe_inverse.append(i)

    return righe_inverse

# print("=== negativo ===")
# print(negativo(immagine))

# print("=== schiarisci ===")
# print(schiarisci(immagine, 25))

# print("=== pixel medi ===")
# print(pixel_medi(immagine))

print("=== righe inverse ===")
print(specchio_verticale(immagine))