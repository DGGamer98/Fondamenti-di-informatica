eta = int(input("Inserisci l'eta: "))
invito = input("Hai l'invito?: ")

if eta >= 18 or invito == "si":
    print("Accesso consentito")
else:
    print("Accesso negato")
