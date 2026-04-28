user=[]

'''Function for support'''

def log_operazione(function):
    def wrapper(*args, **kwargs):
        print(f"[GYM LOG :) ] {function.__name__} in corso")
        result = function(*args, **kwargs) 
        print("[GYM LOG ;)  ] operazione completata ")
        return result
    return wrapper

def controllo_lista_vuota(function):
    def wrapper(*args, **kwargs):
        lista = args[1]
        if len(lista) == 0:
            print("[ERROR lista vuota]")
            return
        return function(*args, **kwargs)
    return wrapper

def valida_abbonamento(function):
    def wrapper(*args, **kwargs):
        abbonamento = args[2]
        if abbonamento ==  "base" or "premium" or "vip":
            print("[GYM LOG] Abbonamento valido")
        else:
            print("[GYM Error] abbonamento non valido")
            return
        return function(*args, **kwargs)
    return wrapper


'''Operations function'''

@log_operazione
def aggiungi_membro(membri, nome, abbonamento):
    #struttura del dizionario
    membro = {
        "id": len(membri) + 1,
        "nome": nome,
        "abbonamento": abbonamento,
        "accessi":0,
        "attivo":True,
        "corsi":[]
    }
    
    membri.append(membro)
 
@log_operazione
@controllo_lista_vuota
def registra_accesso(membri, nome):
    for membro in membri:
        if (nome == membro["nome"]) and (membro["attivo"] == True):
            membro["accessi"]+=1
        elif membro["attivo"] == False:
            print("Abbonamento scaduto")
            return
        else:
            print("Nome non trovato nel database ")
            
def iscrivi_corso(membri, nome, corso):
    corsi = []
    #controllo i vari abbonamenti per i corsi
    for membro in membri:
        if nome == membro["nome"]:
            if corso not in corsi:
                if membro["abbonamento"] == "base":
                    print("[Attenzione] poichè si a un abbonamento base ti puoi iscrivere solo a 2 corsi")
                    for corso in range(0,2):
                        corso = input("add corso massimo 2: ")
                        corsi.append(corso)
                        print("corso aggiunto")
                elif (membro["abbonamento"] == "premium") or (membro["abbonamento"] == "vip"):
                    for corso in range(0,12):
                        corso = input("add corso: ")
                        corsi.append(corso)
                        print("corso aggiunto")
    membro["corsi"] = corsi

def disattiva_membro(membri, nome):
    for membro in membri:
        if nome == membro["nome"]:
            membro["attivo"] = False
            membro["corsi"].clear() # elimino il contenuto (si può usare anche  = [])
            print("[LOG] abbonamento disattivato")
        else:
            print("[ERROR] errore")


def report_generale(membri):
    totaleMembri = len(membri)
    totaleAttivi = []
    totaleScaduti = []

    for m in membri:
        if m["attivo"] == True:
            totaleAttivi.append(m)
        elif m["attivo"] == False:
            totaleScaduti.append(m)
        
        if m["accessi"] > m["accessi"]:
            print(f"il membdro {m["nome"]} a più accessi di tutti")
    
    #uso len per il totale di abbonamenti attivi o disattivi nella palestra
    abbonamenti_attivi = len(totaleAttivi)
    abbonamenti_scaduti = len(totaleScaduti)
    
    print(f"totalte abbonamenti attivi {abbonamenti_attivi}")
    print(f"totale abbonamenti scaduti {abbonamenti_scaduti}")
    print(f"membri totale {totaleMembri}")
      
def stampa(membri):
    for x in membri:
        corsi = ", ".join(x["corsi"]) #join unisco una sequena alla stringa principale
        print(f"ID: {x["id"]} | Nome: {x["nome"]} | Abbonamento: {x["abbonamento"]} | Accessi: {x["accessi"]} | Corsi {corsi}")

#iterazione infinita controllata
while True:
    print("1 aggiungi membro")
    print("2 Registro accessi")
    print("3 Iscrizione corsi")
    print("4 Stampa")
    print("5 disattiva abbonamento")
    print("6 report generale")
    
    
    scelta = int(input("> "))
    
    #switch case menu interattivo
    if scelta == 1:
        nome = input("Nome: ")
        abbonamento = input("abbonamento: ")
        aggiungi_membro(user, nome, abbonamento)
    elif scelta == 2:
        nomeAccesso = input("accesso di: ")
        registra_accesso(user, nomeAccesso)
    elif scelta == 3:
        nomeAbbonato = input("Nome: ")
        iscrizione_corso = input("iscrizione corso: ")
        iscrivi_corso(user, nomeAbbonato, iscrizione_corso)
    elif scelta == 4:
        stampa(user)
    elif scelta == 5:
        nome = input("Abbonamento da disattivare: ")
        disattiva_membro(user, nome)
    elif scelta == 6:
        report_generale(user)
        



aggiungi_membro(user, "Davide", "base")
registra_accesso(user,"Davide")

stampa(user)
       
    


