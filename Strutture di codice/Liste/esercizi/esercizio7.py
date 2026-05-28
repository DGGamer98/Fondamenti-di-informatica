'''Creare una nuova lista che contenga gli elementi con indici dispari della lista precedente.'''
myList = [10, 5, 2, 8, 6, 2, 7]
num_Dispari = []

for x in myList:
    if x % 2 == 1:
        num_Dispari.append(x)
        
print(num_Dispari)