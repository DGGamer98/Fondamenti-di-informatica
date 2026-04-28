'''Il programma deve continuare a leggere numeri naturali e a calcolarne la somma, fermandosi quando legge uno zero'''

while True:
    numero1 = int(input("numero1: "))
    numero2 = int(input("numero2: "))
    
    if numero1 == 0 or numero2 == 0:
        break
    
    somma = numero1 + numero2

    print(somma)