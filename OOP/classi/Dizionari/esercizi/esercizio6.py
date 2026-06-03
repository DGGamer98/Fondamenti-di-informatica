'''Creare una nuova lista che contenga solo le chiavi del dizionario precedente.'''
persona = {
    "nome":"Mario",
    "cognome":"Rossi",
    "eta":30
}

key_List = []

#prendo solo le chiavi del dizionario
for x in persona.keys():
    key_List.append(x)

#scorro dentro la lista
for x in key_List:
    print(x)

