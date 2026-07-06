numeriRighe = 3
numeriColonne = 4

m = [] #lista vuota che conterrà le righe della matrice

for i in range(numeriRighe): 
    n = []
    for j in range(numeriColonne):
        n.append(0)
    m.append(n)
print("m: ", m)

'''
Dietro le quinte:

i=0 → n=[] → aggiungo 0,0,0,0 → n=[0,0,0,0] → m=[[0,0,0,0]]
i=1 → n=[] → aggiungo 0,0,0,0 → n=[0,0,0,0] → m=[[0,0,0,0],[0,0,0,0]]
i=2 → n=[] → aggiungo 0,0,0,0 → n=[0,0,0,0] → m=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
'''