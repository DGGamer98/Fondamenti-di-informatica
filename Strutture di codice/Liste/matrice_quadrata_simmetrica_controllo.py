dimensione = 4
m=[[1,2,3,4],
   [2,3,5,0],
   [3,5,6,8],
   [4,0,8,0]]

simmetrica = True

for i in range(dimensione):
    for j in range(i):
        if m[i][j] != m[i][j]:
            simmetrica=False
        
if simmetrica:
    print("La matrice è simmetrica")
else:
    print("La matrice non è simmetrica")