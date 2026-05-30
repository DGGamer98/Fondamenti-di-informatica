#Struttura dizionaro
#Dizionario è una collezione di coppie chiave-valore

#creazione di un dizionario
persona = {
    "nome":"Davide",
    "cognome":"Gatta",
    "eta":23
}

#Leggere un valore 
print(persona["nome"])

#Modifica il valore esistente
persona["eta"] = 26
print(persona["eta"])

#Aggiungere una nuova chiave
persona["citta"] = "Roma"
print(persona)

#eliminazione chiave
del persona["eta"]
print(persona)

#Stampo tutte le chiavi
print(persona.keys())

'''per stampare in colonna'''
for x in persona.keys():
    print(x)

#Stampo i valori
print(persona.values())
for x in persona.values():
    print(x)

#Stampo sia chiave che valore
print(persona.items())
for x in persona.items:
    print(x)

'''Pattern molto utile --> lista di dizionari'''
myList = [
    {"nome":"mario","cognome":"rossi"},
    {"nome":"luca","cognome":"verdi"}
]

for x in myList:
    if x["nome"] == "mario":
        x["nome"] = "ludovico"
    
print(myList)