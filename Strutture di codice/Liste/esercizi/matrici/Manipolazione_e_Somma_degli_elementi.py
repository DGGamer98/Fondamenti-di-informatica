matrix = [
    [7,8,6],
    [9,5,8],
    [6,7,10]
]


#modifica elemento
matrix[1][2] = 7

#Estrazione di un elemento
element = matrix[1][2]
print(f"Elemento estratto {element}")


#Somma elementi della matrice
counter = 0
for i in matrix:
    for j in i:
        counter+=j

print(f"Somma elementi matrice {counter}")

#stampo tutta la matrice
for i in matrix:
    print(i)

#print(matrix)


