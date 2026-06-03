''' Il programma deve continuare a leggere numeri naturali e a calcolarne la somma, fermandosi quando legge uno zero.'''

somma = 0

while True:
    numero1 = int(input("Numero1: "))
    numero2 = int(input("Numero2: "))

    if numero1 == 0 or numero2 == 0:
        break
    
    somma = numero1 + numero2
    print(somma)
