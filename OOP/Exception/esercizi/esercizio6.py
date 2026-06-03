'''Scrivere un programma che tenta di convertire una stringa in un tipo di dato non appropriato, 
   gestendo l'eccezione.'''


dato_da_convertire = input("dato da convertire: ")


try: 
    #dato_convertito = int(len(dato_da_convertire))
    dato_convertito = int(dato_da_convertire)
    print("il dato è stato convertito in:", type(dato_convertito))
except ValueError as e:
    print("Il dato non è convertibile", e)
