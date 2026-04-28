def conta_parole(frase):
    counter = 0
    for i in frase.split():
        counter+=1
    return f"Ci sono {counter} parole"
        

def conta_caratteri(frase):
    couter = 0
    for char in frase:
        couter+=1
    return f"Ci sono {couter} lettere"


def inverti_frase(frase):
    parole = frase.split()
    inversa = " ".join(parole[::-1])#Inverto la lista e riunisco
    print(inversa)

def parola_più_lunga(frase):
    paroleLunghe = []
    
    for char in frase.split():
        if len(char) > 5:
            paroleLunghe.append(char)
    return f"Ecco le parole più lunghe {paroleLunghe}"

def contiene_parola(frase):
    parola = frase.split()
    searchParola = input("> ")
    counter = 0
    for char in parola:
        counter +=1
        if searchParola == char:
            return True
    return False
    
    
while True:
    
    print(" 1) conta_parole")
    print(" 2) conta_caratteri")
    print(" 3) inverti_frase")
    print(" 4) parola_più_lunga")
    print(" 5) contiene_parola")
    
    scelta = int(input("> "))
    
    if scelta == 1:
        frase = input("Inserisci la frase: ")
        print(conta_parole(frase))
    elif scelta == 2:        
        frase = input("Inserisci la frase: ")
        print(conta_caratteri(frase))
    elif scelta == 3:
        frase = input("Inserisci la frase: ")
        inverti_frase(frase)
    elif scelta == 4:
        frase = input("Inserisci la frase: ")
        print(parola_più_lunga(frase))
    elif scelta == 5:
        frase = input("Inserisci la frase: ")
        print(contiene_parola(frase))
