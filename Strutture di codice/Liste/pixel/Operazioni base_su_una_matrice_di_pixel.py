immagine = [
    [200, 100, 50, 254],
    [80, 150, 200, 30],
    [255, 20, 100, 180],
    [10, 220, 75, 140]
]

#Ricorda: immagine[y][x] --> riga y, colonna x

def stampa_immagine(immagine):
    for y in immagine:
        print(y)

def pixel_piu_luminoso(immagine):
    pixel_luminoso = immagine[0][0]  #Variabile supporto
    pos_y = 0
    pos_x = 0

    for y in range(len(immagine)):
        for x in range(len(immagine[y])):
            valore = immagine[y][x]

            if valore > pixel_luminoso:
                pixel_luminoso = valore
                pos_y = y
                pos_x = x        
    return f"Il pixel più luminoso: {pixel_luminoso} in posizione {pos_y}, {pos_x}"

def applica_soglia(immagine, soglia):
    new_immagine = []

    for y in immagine:
        for x in y:
            valore = x

            if valore >= soglia:
                valore = 255
                new_immagine.append(valore)
            elif valore < soglia:
                valore = 0
                new_immagine.append(valore)
    return new_immagine

def riga_media(immagine, y):
    totale_value = 0
    counter = 0
    for y in range(len(immagine[y])):
        totale_value+=y
        counter+=1

    media_riga = totale_value/counter
    return media_riga
    



stampa_immagine(immagine)
print(pixel_piu_luminoso(immagine))
print(applica_soglia(immagine, 145))
print(riga_media(immagine, 2))
