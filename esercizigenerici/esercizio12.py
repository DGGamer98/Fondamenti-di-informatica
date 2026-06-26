'''Validazione password
Scrivi una funzione che controlla se una password è valida. Una password è valida se:

Ha almeno 8 caratteri
Contiene almeno una lettera maiuscola
Contiene almeno una lettera minuscola
Contiene almeno un numero
Contiene almeno un carattere speciale (!, @, #, $, %)'''

password = "ciao@@#Peppo34"

def analisi_password(password):
    lunghezza = len(password)

    if lunghezza < 8:
        print("Password troppo corta")
        return False

    #controllo lettere maiuscole
    counterMaius = 0
    for x in password:
        if x.isupper():
            counterMaius+=1

    #controllo lettere minuscole
    countermin = 0
    for y in password:
        if y.islower():
            countermin+=1

    #controllo numeri
    counternum = 0
    for num in password:
        if num.isdigit():
            counternum+=1

    #caratteri speciali
    if not password.isalnum():
        print("ci sono dei caratteri speciali")
    else:
        print("non ci sono caratteri speciali")
            
    print(f"ci sono {counterMaius} lettere maiuscole")
    print(f"ci sono {countermin} lettere minuscole")
    print(f"ci sono {counternum} numeri")

analisi_password(password)