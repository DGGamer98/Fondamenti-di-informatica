'''Creare una nuova lista che contenga solo i primi tre elementi della lista precedente.'''

myList = [10, 5, 2, 8, 6, 2]
newList = []

newList.append(myList[:3])

print(newList)