import math

def teomeraPitagora(a,b):
    i = math.sqrt(a*a + b*b) # i sta per ipotenusa
    print("ipotenusa", i)
    

a = int(input("Cateto maggiore: "))
b = int(input("Cateto minore: "))

teomeraPitagora(a,b)