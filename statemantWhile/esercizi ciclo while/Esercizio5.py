pari = 0
disapri = 0

while True:
    numero1 = int(input("Numero 1 "))
    numero2 = int(input("Numero 2 "))

    #se una delle due variabili è zero esce dal programma
    if  numero1 == 0 or numero2 == 0:
        break

    somma = numero1 + numero2
    print(somma)

    if somma % 2 == 0:
        print(f"somma pari{somma}")
        pari+=1
        print(f"numeri pari trovati: {pari}")
    else:
        print(f"somma dispari {somma}")
        disapri+=1
        print(f"Numeri dispari trovati: {disapri}")




