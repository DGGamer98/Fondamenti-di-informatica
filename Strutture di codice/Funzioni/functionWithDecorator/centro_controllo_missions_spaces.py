import random

listMission = []

'''Function support'''
def log_operation(function):
    def wrapper(*args, **kwargs):
        print("[LOG] operation in progress")
        result = function(*args, **kwargs)
        print("[LOG] operation finished")
        return result
    return wrapper


def controllo_lista_vuota(function):
    def wrapper(*args, **kwargs):
        lista = args[0]
        if len(lista) == 0:
            print("This list is empty")
            return 
        return function(*args, **kwargs)
    return wrapper


def valida_stato(function):
    def wrapper(*args, **kwargs):
        lista = args[2]
        if lista == "attiva" or "in pausa" or"completata" or "fallita":
            print("Stato valido")
        else:
            print("Stato non valido")
            return
        return function(*args, **kwargs)
    return wrapper



'''Operations function'''

@log_operation
def add_mission(missioni, nome, destinazione, equipaggio):
    nuova_missione = {
        "id" : len(missioni) + 1,
        "nome": nome,
        "destinazione":destinazione,
        "giorni": random.randint(0, 25),
        "stato": "attiva",
        "carburante": random.randint(0,100),
        "equipaggio":equipaggio
   }
    
    for m in missioni:
        if m["id"] == nuova_missione["id"]:
            print("Una missione con questo ID esiste già")
            return
    
    missioni.append(nuova_missione)
    
@log_operation
@controllo_lista_vuota
def show_missions(missioni):
    for m in missioni:
        membro = ", ".join(m["equipaggio"]) #unione di una lista di stringhe per formattare una nuova stringa
        print(f"ID: {m['id']} | Nome: {m['nome']} | Destinazione: {m['destinazione']} | giorni: {m['giorni']} | stato: {m['stato']} | carburante: {m['carburante']}% | Equipaggio: {membro}")

@log_operation
@controllo_lista_vuota
@valida_stato
def update_status(missioni,nome, new_stato):
    for m in missioni:
        if m["nome"] == nome:
            m["stato"] = new_stato
            print("[LOG] stato aggiornato")
        
        if m["stato"] == "":
            print("[ERROR] this status is invalid")
        
@log_operation
@controllo_lista_vuota
def add_equipaggio(missioni, nome, new_equipaggio):
    for m in missioni:
        if m["nome"] == nome:
            if new_equipaggio in m["equipaggio"]:
                print("membro già presente")
            else:
                m["equipaggio"].append(new_equipaggio)
                
@log_operation
@controllo_lista_vuota
def consumo_carburante(missioni, nome, status_error):
    quantità = 100
    for m in missioni:
        if m["nome"] == nome:
            m["carburante"] -= quantità
            if (m["carburante"] < 20) and (m["carburante"] > 0): 
                print("[Error] carburante sotto il 20%")
            elif m["carburante"] == 0:
                print("[fatal error] missione annullata")
                m["stato"] = status_error
                
@log_operation
@controllo_lista_vuota
def report_generale(missioni, stato):
    missionPause = 0
    completed = 0
    failed = 0
    active = 0
    missione_più_lunga = missioni[0]
    
    totaleMissioni = len(missioni)
    print(f"missioni totali {totaleMissioni}")
    
    for m in missioni:
        if m["stato"] == stato:
            active+=1
        elif m["stato"] == stato:
            missionPause+=1
        elif m["stato"] == stato:
            completed+=1
        elif m["stato"] == stato:
            failed+=1
    
    for m in missioni:
        if m["giorni"] > missione_più_lunga["giorni"]:
            print(f"La missione più lunga è di {m}")
        
        if m["carburante"] < 20:
            print(f"Missione con carburante critico {m}")
    
        
            
        
    print(f"vi sono {active} missioni in esecuzione")
    print(f"vi sono {completed} missioni completate")
    print(f"vi sono {failed} missioni fallite")
    print(f"vi sono {missionPause} missioni in pausa")

    
while True:
    print("1 aggiungi missione")
    print("2 show missions")
    print("3 update status")
    print("4 add equipaggio")
    print("5 consumo carburante")
    print("6 report generale")
    
    scelta = int(input("> "))
    
    if scelta == 1:
        nome = input("nome: ")
        destinazione = input("destinazione: ")
        
        equipaggio = []
        
        numeroEquipaggio = int(input("> "))
        for x in range(0, numeroEquipaggio):
            x = input("equipaggio: ")
            if x not in equipaggio:
                equipaggio.append(x)
        add_mission(listMission, nome, destinazione , equipaggio)
    elif scelta == 2:
        show_missions(listMission)




#update_status(listMission, nome="Apollo-X", new_stato="disable")

#add_equipaggio(listMission, nome="Apollo-X", new_equipaggio="Rossi")

#consumo_carburante(listMission, nome="Apollo-XY", status_error="error")
show_missions(listMission)  

report_generale(listMission,stato="attiva")


