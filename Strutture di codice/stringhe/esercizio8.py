'''Assegnare una stringa "Ciao mondo" ad una variabile "stringa" e utilizzare il metodo count() 
   per contare il numero di volte in cui la lettera "o" appare nella stringa.'''

Stringa = "Ciao mondo"
counter = 0

#metodo 1
newStriga = Stringa.count("o")
print(newStriga)


#metodo 2
for x in Stringa:
    if x == "o":
        counter+=1
print(counter)



