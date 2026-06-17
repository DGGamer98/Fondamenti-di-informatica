numeriRighe = 3
numeriColonne = 4

m = []

for i in range(numeriRighe):
    n = []
    for j in range(numeriColonne):
        n.append(j)
    m.append(n)
print("m: ", m)