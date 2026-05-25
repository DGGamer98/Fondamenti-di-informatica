missioni = []

def log_missione(funzione):
    def wrapper(*args, **kwargs):
        print(f"[LOG] operazione in corso {funzione.__name__}")
        result = funzione(*args, **kwargs)
        print("[LOG] operazione terminata")
        return result
    return wrapper

def verifica_missioni_vuote(funzione):
    def wrapper(*args, **kwargs):
        lista =  args[0]
        if len(lista) == 0:
            print("This list is empty")
            return
        return funzione(*args, **kwargs)
    return wrapper

''' Function operator '''

@log_missione
def aggiungi_missione(nome, destinazione, stato, equipaggio):
    nuova_missione = {
        "nome":nome,
        "destinazione": destinazione,
        "stato": stato,
        "equipaggio": equipaggio,
        "durata_giorni": 0
    }
    
    missioni.append(nuova_missione)
    print(f"Missione {nuova_missione} aggiunta")

@log_missione
@verifica_missioni_vuote
def mostra_missioni(missione):
    for x in missione:
        print(x)

@log_missione
@verifica_missioni_vuote
def aggiorna_stato(missione, nome, nuovo_stato):
    for x in missione:
        if x["nome"] == nome:
            x["stato"] = nuovo_stato
            print("[LOG] stato aggiornato")
    return aggiorna_stato

@log_missione
@verifica_missioni_vuote
def aggiorna_durata(missione, nome, new_giorni):
    for x in missione:
        if x["nome"] == nome:
            x["durata_giorni"] += new_giorni
            print("[LOG] durata giorni aggiornata")
    return aggiorna_durata

@log_missione
@verifica_missioni_vuote
def mostra_per_stato(missioni, stato):
    for x in missioni:
        if x["stato"] == stato:
            print(x)

while True:
    print("1 aggiungi missione")
    print("2 mostra missione")
    print("3 aggiorna stato")
    print("4 aggiorna durata")
    print("5 mostra_per_stato")
    print("6 esci")
    
    scelta = int(input("> "))
    
    if scelta == 1:
        nome = input("nome: ")
        destinazione = input("destinazione: ")
        stato = input("stato: ")
        equipaggio = input("equipaggio: ")
        
        aggiungi_missione(nome, destinazione, stato, equipaggio)
    elif scelta == 2:
        mostra_missioni(missioni)
    elif scelta == 3:
        nome = input("nome: ")
        nuovo_stato = input("nuovo stato: ")
        
        aggiorna_stato(missioni, nome, nuovo_stato)
    elif scelta == 4:
        nome = input("nome: ")
        new_giorni = int(input("new giorni: "))
        
        aggiorna_durata(missioni, nome, new_giorni)
    elif scelta == 5:
        stato = input("mostra per stato: ")
        
        mostra_per_stato(missioni, stato)
    elif scelta == 6:
        break
        