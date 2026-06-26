'''Controllare che una stringa inizi o finisca per \. Ci sono almeno due modi.'''



myString = "ciao mondo \ "

if myString.startswith("\ "):
    print("ok")
elif myString.endswith("\ "):
    print("ok 2")
else:
    print("False")
