'''Creare una stringa che abbia, come testo, cinque spazi'''
myString = " " + " " + " " + " " + " "
#myString = " "*5
print(len(myString))

#controllo che la stringa contenga almeno uno spazio
if " " in myString:
    print("ok")
else:
    print("No")