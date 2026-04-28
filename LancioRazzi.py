from datetime import datetime
import time

def log_lancio(funzione):
    def wrapper(*args, **kwargs):
        print(f"[Date] {funzione.__name__} {datetime.now().strftime('%H:%M:%S')}")
        resutl = funzione(*args, **kwargs)
        print(f"[Date] {funzione.__name__} {datetime.now().strftime('%H:%M:%S')}")
        return resutl
    return wrapper

def controllo_pronto(funzione):
    def wrapper(*args, **kwargs):
        if args[0].stato != "stato":
            print("[Error] razzo non pronto!")
            return
        return funzione(*args, **kwargs)
    return wrapper

#COMPOSIZIONE - ScatolaNera appartiene al Razzo
class ScatolaNera:
    def __init__(self):
        self.eventi = []
        
    def registra(self, evento):
        time = datetime.now().strftime('%H:%M:%S')
        self.eventi.append(f"{time} - {evento}")
        print("[Event] evento registrato")
        
    def mostra_log(self):
        for x in self.eventi:
            print(f"[LOG] {x}")

#EREDITARIETA'        
class VeicoloASpaziale:
    def __init__(self, nome, carburante):
        self.nome = nome
        self.carburante = carburante
        self.stato = "in preparazione"
        
    def __str__(self):
        return f"| Nome veicolo: {self.nome} | stato: {self.stato} | carburante: {self.carburante} |"
    
class Razzo(VeicoloASpaziale): #eredita la classe VeicoloASpaziale
    contatore = 1
    
    def __init__(self, nome, carburante):
        super().__init__(nome, carburante)
        self.id = Razzo.contatore
        Razzo.contatore +=1 # incremento di uno ogni istanza
        self.scatolaNera = ScatolaNera() #Composizione
        self.payload = []
    
    @log_lancio
    def aggiungi_payload(self, satellite):
        
        if self.stato != "in preparazione":
            print("[ERROR] non puoi aggiungere payload")
            
        if satellite in self.payload:
            print("[LOG] Satellite già presente")
            
        if len(self.payload) > 4:
            print("[Error] puoi aggiungere solo 4 satelliti")
        else:
            self.payload.append(satellite)
            print("[LOG] satellite aggiunto")
            self.scatolaNera.registra(satellite)
    
    @log_lancio
    def segna_pronto(self):
        if len(self.payload) == 0:
            print("[LOG] Nessun payload a bordo")
        else:
            self.stato = "pronto"
            self.scatolaNera.registra(self.stato)
            
    def lancia(self):
        for x in range(10, 0, -1):
            time.sleep(1.1)
            print(x)
        self.stato = "Lanciato"
        self.scatolaNera.registra(self.stato)
        print("[LOG] Lancio avvenuto")
        
    def __str__(self):
        return f" nome: {self.nome} | carburante: {self.carburante} | payload: {self.payload}"
    

class Sonda(VeicoloASpaziale):
    def __init__(self, nome, carburante, destinazione):
        super().__init__(nome, carburante)
        self.destinazione = destinazione
        self.distanza_percorsa = 0
        
    def avanza(self, km):
        self.distanza_percorsa+=km

        consumo = km/100
        self.carburante -= consumo
        
        if self.carburante <= 0:
            self.carburante = 0
            self.stato = "fuori servizio"
        
        print(f"[LOG] la sona {self.nome} ha percorso {self.distanza_percorsa} | {self.carburante}")
        
    def __str__(self):
        return f"Nome: {self.nome} | Destinazione: {self.destinazione} | {self.distanza_percorsa}km | Carburante {self.carburante}"
    

class CentroLancio:
    def __init__(self, nome):
        self.nome = nome
        self.razzi = []
        self.sonde = []
        
    def aggiungi_razzo(self, razzo):
        self.razzi.append(razzo)
        print("[LOG] Razzo già registrato")
    
    def aggiungi_sonda(self, sonda):
        self.sonde.append(sonda)
        print("[LOG] Sonda già presente ")
        
    '''def tecnico_ispeziona(self, tecnico, razzo):  # ASSOCIAZIONE
    # stampa "Tecnico X ispeziona il razzo Y"
    # mostra il log della scatola nera del razzo

    @log_lancio
    def report_centro(self):
        # stampa nome centro
        # stampa tutti i razzi con stato
        # stampa tutte le sonde con stato
        # stampa quanti razzi sono già stati lanciati'''
        
    
            
        
r1 = Razzo("Vega-C", 100)
r2 = Razzo("Ariane-6", 100)        
        
r1.aggiungi_payload("SICRAL-1")
r1.aggiungi_payload("COSMO-SkyMed")

r1.segna_pronto()

r1.lancia()