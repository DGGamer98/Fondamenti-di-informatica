immagine = [
    [255,   0, 128,  64],
    [ 32, 200,  96, 160],
    [192,  48, 224,  16],
    [ 80, 240, 112, 176]
]

def somma_bordi(immagine):
    lista_riga = []
    somma_colonna = 0
    somma_riga = 0
    
    for i in range(len(immagine)):
        if (immagine[i] == immagine[0]): #confronto gli indici di elemento i esimo con gli indici di riga superiore ed inferiore
            lista_riga = immagine[i] + immagine[3]
            print(type(lista_riga))
            #non uso sum() faccio la somma a mano con un iteratore
            for x in lista_riga:
                somma_riga+=x 
                        
        for j in range(len(immagine[0])):
            if immagine[i][0] == immagine[i][j]:
                ultima_colonna = immagine[i][3] # racchiudo l'ultima colonna in una variabile
                #print(immagine[i][j], ultima_colonna)
                somma_colonna= immagine[i][j] + ultima_colonna
                
    return f"somma riga {somma_riga}, somma colonna {somma_colonna}"

def quadrante(immagine, q):
    for i in range(len(immagine)):
        for j in range(len(immagine[0])):
            if q == 1:
                if i < len(immagine)/2 and j < len(immagine[0])/2:
                    print(immagine[i][j], end=" ")
            elif q == 2:
                if i < len(immagine)/2 and j >= len(immagine[0])/2:
                    print(immagine[i][j], end=" ")
            elif q == 3:
                if i >= len(immagine)/2 and j < len(immagine[0])/2:
                    print(immagine[i][j], end=" ")
            elif q == 4:
                if i >= len(immagine)/2 and j >= len(immagine[0])/2:
                    print(immagine[i][j], end=" ")

def scambia_quadranti(immagine):
    new_list = []
    q = int(input("Numero da 1 a 4: "))
    for i in range(len(immagine)):
        for j in range(len(immagine[0])):
            if q == 1:
                if i < len(immagine)/2 and j < (len(immagine[0]))/2:
                    new_list.append(immagine[i][j])
            elif q == 2:
                if i < len(immagine)/2 and j >= (len(immagine[0]))/2:
                    new_list.append(immagine[i][j])
            elif q == 3:
                if i >= len(immagine)/2 and j < (len(immagine[0]))/2:
                    new_list.append(immagine[i][j])
            elif q == 4:
                if i >= len(immagine)/2 and j >= (len(immagine[0]))/2:
                    new_list.append(immagine[i][j])
    # counter = 0
    # while counter <= 4:
    #     counter+=1
    #     q = int(input("Numero da 1 a 4: "))
    #     for i in range(len(immagine)):
    #         for j in range(len(immagine[0])):
    #             if q == 1:
    #                 if i < len(immagine)/2 and j < (len(immagine[0]))/2:
    #                     new_list.append(immagine[i][j])
    #             elif q == 2:
    #                 if i < len(immagine)/2 and j >= (len(immagine[0]))/2:
    #                     new_list.append(immagine[i][j])
    #             elif q == 3:
    #                 if i >= len(immagine)/2 and j < (len(immagine[0]))/2:
    #                     new_list.append(immagine[i][j])
    #             elif q == 4:
    #                 if i >= len(immagine)/2 and j >= (len(immagine[0]))/2:
    #                     new_list.append(immagine[i][j])
            
    print(new_list)
            

def contrasto(immagine, fattore):
    lista_contrasto = []
    for i in range(len(immagine)):
        for j in range(len(immagine[0])):
            pixel = immagine[i][j]*fattore
            if pixel > 255: #il singolo pixel non può andare oltre
                pixel = 255
            elif pixel < 0:
                pixel = 1
            lista_contrasto.append(pixel)
    return lista_contrasto
        
        
# print("=== somma bordi ===")
# print(somma_bordi(immagine))

# print("=== quadrante ===")
# quadrante(immagine, 1)

# print("=== scambia quadranti ===")
# scambia_quadranti(immagine)

print("=== contrasto ===")
print(contrasto(immagine, 2))