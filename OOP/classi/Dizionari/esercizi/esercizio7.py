'''Creare una nuova lista che contenga solo i valori del dizionario precedente.'''
persona = {
    "nome":"Mario",
    "cognome":"Rossi",
    "eta":30
}

lista_value = []

for x in persona.values():
    lista_value.append(x)

#o anche cosi
lista_value.append(persona.values())
    
print(lista_value)