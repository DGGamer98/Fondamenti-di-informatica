listStudent = []
list_Student_Present = []
list_Student_NotPresent = []


#create function decorator
def log_operazione(function):
    def wrapper(*args, **kwargs):
        print("[LOG] Eseguendo l'operazione")
        resutl = function(*args, **kwargs)
        print("[LOG] operazione completata")
        return resutl
    return wrapper

@log_operazione
def aggiungi_studente(nome):
    listStudent.append(nome)
    

@log_operazione
def senga_presente(nome):
    for x in listStudent:
        if nome == x:
            list_Student_Present.append(nome)
    

@log_operazione
def segna_assente(nome):
    if nome not in list_Student_Present:
        list_Student_NotPresent.append(nome)
   

@log_operazione
def mostra_assenti():
    print("Lista assenti") 
    for x in list_Student_NotPresent:
        print(x)
    

@log_operazione
def mostra_presenti():
    print("Lista presenti")
    for x in list_Student_Present:
        print(x)
    
        


while True:
    print("=== Menu ===")
    
    print("1 Aggiungi studente")
    print("2 Segna presente")
    print("3 Segna Assente")
    print("4 Mostra presenti")
    print("5 Mostra assenti")
    print("0 esci")
    
    scelta = int(input("> "))
    
    if scelta == 1:
        nome = input("Nome: ")
        aggiungi_studente(nome)
    elif scelta == 2:
        nome = input("Nome: ")
        senga_presente(nome)
    elif scelta == 3:
        nome = input("Nome")
        segna_assente(nome)
    elif scelta == 4:
        mostra_presenti()
    elif scelta == 5:
        mostra_assenti()
    elif scelta == 0:
        break


            
        