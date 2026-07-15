immagine = [
    [200, 50,  30, 255],
    [ 80, 170, 20, 100],
    [255, 90,  60, 140],
    [ 10, 200, 80, 180]
]

new_image = []
new_pixel = []

def negativo(immagine):
    nuovo_valore = 255
    for y in range(len(immagine)):
        n=[]
        for x in range(len(immagine[0])):
            new_value = nuovo_valore - immagine[y][x]
            n.append(new_value)
        
        new_image.append(n)
               
    for y in new_image:
        print(y) 
    
def applica_soglia(immagine, soglia):
    for y in range(len(immagine)):
        n = []
        for x in range(len(immagine[0])):
            if immagine[y][x] >= soglia:
                immagine[y][x] = 255
                n.append(immagine[y][x])
            elif immagine[y][x] < soglia:
                immagine[y][x] = 0
                n.append(immagine[y][x])
        new_pixel.append(n)
        
    for y in new_pixel:
        print(y) 


print(negativo(immagine))
applica_soglia(immagine, 50)