'''Contare il numero di occorrenze dell'elemento "mela" nella tupla precedente.'''

myTupla = ("Pizza", "mela", "mela")

counter = 0
for x in myTupla:
    if x == "mela":
        counter+=1
        continue

print(f"le mele sono {counter}")