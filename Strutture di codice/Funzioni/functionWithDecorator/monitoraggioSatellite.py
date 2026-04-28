listaSatellite = []

#funzioni decorator
def log_operazione(funzione):
    def wrapper(*args, **kwargs):
        print(f"[LOG] operazione in corso {funzione.__name__}")
        result = funzione(*args, **kwargs)
        print("[LOG] operazione in terminata")
        return result
    return wrapper

def controllo_flotta_vuota(funzione):
    def wrapper(*args, **kwargs):
        lista = args[0]
        if len(lista) == 0:
            print("[Error] this list is empty")
            return
        return funzione(*args, **kwargs)
    return wrapper

'''Function for operation'''

@log_operazione
def add_Satellite(nome, orbita, stato, carburante):
    satellite = [nome, orbita, stato, carburante]
    listaSatellite.append(satellite)
    
@log_operazione
@controllo_flotta_vuota
def stampa_flotta(satelliti):
    for s in satelliti:
        print(f"- {s[0]} | Orbita: {s[1]} | Stato: {s[2]} | Carburante: {s[3]}%")
    

@log_operazione
@controllo_flotta_vuota
def update_status(satelliti, nome, nuovo_stato):
    for satellite in satelliti:
        if satellite[0] == nome:
            satellite[2] = nuovo_stato
            print(satellite)
        
@log_operazione
@controllo_flotta_vuota    
def consuma_carburante(satelliti, nome, quantita):
    for satellite in satelliti:
        if satellite[0] == nome:
            satellite[3] -= quantita
            
            if satellite[3] <= 20:
                print("[Attenzione] carburante poco")
                
            if satellite[3] == 0:
                satellite[3] = 0
                
@log_operazione
@controllo_flotta_vuota            
def mostra_critici(satelliti):
    for satellite in satelliti:
        if satellite[3] <= 20:
            print("critici")
            print(satellite) 

while True:
    print("1. Aggiungi satellite")
    print("2. Stampa flotta")
    print("3. Aggiorna stato")
    print("4. Consuma carburante")
    print("5. Mostra satelliti critici")
    print("6. Esci")
    
    scelta = int(input("> "))
    
    if scelta == 1:
        add_Satellite("SICRAL-1", "GEO", "operativo", 100)
    elif scelta == 2:
        stampa_flotta(listaSatellite)
    elif scelta == 3:
        update_status(listaSatellite, "SICRAL-1", "manutenzione")
    elif scelta == 4:
        consuma_carburante(listaSatellite,"SICRAL-2", 20)
    elif scelta == 5:
        mostra_critici(listaSatellite)
    elif scelta == 6:
        break
    