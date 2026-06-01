persona = {
    "nome":"Mario",
    "cognome":"Rossi",
    "eta":30
}

#Primo modo
counter = 0
for x in persona.keys():
    counter+=1
    
print(f"ci sono {counter} elementi")

#Secondo modo
totElement = len(persona)
print(totElement)