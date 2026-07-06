numeriRighe = 3
numeriColonne = 4

numRiga = 0 # variabile contatore di  supporto
m = []

for i in range(numeriRighe):
    n = []
    numRiga+=1
    print(f"riga: {numRiga}")
    for j in range(numeriColonne):
        valore = int(input("Inersici il valore: "))
        n.append(valore)
    m.append(n)

print("m: ", m)