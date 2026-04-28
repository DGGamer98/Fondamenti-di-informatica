from datetime import datetime
import random

def log_telespazio(funzione):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {funzione.__name__},  {datetime.now().timestamp()}")
        resutl = funzione(*args, **kwargs)
        print(f"[LOG] {funzione.__name__}, {datetime.now().timestamp()}")
        return resutl
    return wrapper

def controllo_operativo(funzione):
    def wrapper(*args, **kwargs):
        if args[0].stato != "operativo":
            print("[LOG] componente non operativa")
            return
        return funzione(*args, **kwargs)
    return wrapper            


'''Codice operativo'''

class SistemaVita:
    def __init__(self):
        self.ossigeno = 100
        self.temperatura = 22.0
        self.pressione = 101.3
        
    def aggiorna(self, ossigeno, temperatura, pressione):
        #controllo anomalie per i sistemi vita
        if ossigeno < 20:
            print("[ALERT] Ossigeno critico")
            return
        if (temperatura < 18.0) or (temperatura > 26):
            print("[ALERT] Temperatura anomala")
            return
        if (pressione < 50.0) or (pressione > 190.0):
            print("[ALERT] Anomalia nella pressione controllare")
            return

        #modifica del dato negli attributi di istanza
        self.ossigeno = ossigeno
        self.temperatura = temperatura
        self.pressione = pressione

    def mostra(self):
        return f"Parametri del modulo | Ossigeno: {self.ossigeno} | temperatura: {self.temperatura} | pressione: {self.pressione} |"
    
class ComponenteStazione:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.stato = "operativo"
        
    def __str__(self):
        return f" | {self.nome} | {self.tipo} | {self.stato}"
    
class Modulo(ComponenteStazione):
    def __init__(self, nome, tipo):
        super().__init__(nome, tipo)
        self.sistemaVita = SistemaVita() #COMPOSIZIONE --> SistemaVita classe figlia di modulo, inizializata insieme a lui
        self.ore_operative = 0
    
    @log_telespazio
    @controllo_operativo
    def avanza_ore(self, ore):
        self.ore_operative+=ore
        if self.ore_operative >= 500:
            print(f"[MANUTENZIONE] Modulo {self.nome} ha raggiunto {self.ore_operative} ore")
            return
    
    @log_telespazio
    def aggiorna_sistema_vita(self, ossigeno, temperatura, pressione):
        self.sistemaVita.aggiorna(ossigeno, temperatura, pressione)
        
    def __str__(self):
        return f"{self.nome} | {self.tipo} |{self.stato} | {self.ore_operative}"
    

class Astronauta(ComponenteStazione):
    def __init__(self, nome,  nazionalità):
        super().__init__(nome, tipo ="astronauta")
        self.nazionalità = nazionalità
        self.ore_eva = 0
        
    def esegui_eva(self, ore):
        self.ore_eva+=ore
        print(f"[LOG] L'astronauta {self.nome} ha eseguito EVA di {self.ore_eva} ore")
        
    def __str__(self):
        return f"| Nome {self.nome} | Nazionalità: {self.nazionalità} | Ore EVA:{self.ore_eva} |"
    
#AGGREGAZIONE
class StazioneSpaziale:
    def __init__(self, nome):
        self.nome = nome
        self.moduli = []
        self.equipaggio = []
        
    def aggiungi_modulo(self, modulo): #AGGREGAZIONE della classe Modulo
        
        if modulo in self.moduli:
            print("[LOG] il modulo è già presente")
            return

        self.moduli.append(modulo)
        print("[LOG] modulo aggiunto")
    
    def aggiungi_equipaggio(self, astronauta):
        if len(self.equipaggio) >= 6:
            print("Equipaggio al completo!")
            return
        if astronauta in self.equipaggio:
            print("Astronauta già a bordo!")
            return
        self.equipaggio.append(astronauta)  # ← .append() non .aggiungi_equipaggio()!
        print(f"[LOG] {astronauta.nome} aggiunto all'equipaggio")

    
    @log_telespazio
    def mostra_stazione(self):
        print(f"Nome stazione: {self.nome}")
        
        for modulo in self.moduli:
            print(modulo)
             
        for astronuata in self.equipaggio:
            print(astronuata)
            
    @log_telespazio
    def report_sistemi_vita(self):
        print("=== REPORT SISTEMI VITA ===")
        for modulo in self.moduli:
            print(f"\n-- {modulo.nome} --")
            print(modulo.sistemaVita.mostra())  # ← accedi al SistemaVita del modulo
                
    def astronauta_visita_modulo(self, astronauta, modulo):
        print(f"{astronauta.nome} è entrato nel modulo {modulo.nome}")
        print(modulo.sistemaVita.mostra())
        
              
# crea moduli
m1 = Modulo("Columbus", "laboratorio")
m2 = Modulo("Zvezda", "abitativo")

# crea astronauti
a1 = Astronauta("Luca Parmitano", "IT")
a2 = Astronauta("Samantha Cristoforetti", "IT")

# crea stazione e aggiungi (AGGREGAZIONE)
iss = StazioneSpaziale("ISS")
iss.aggiungi_modulo(m1)
iss.aggiungi_modulo(m2)
iss.aggiungi_equipaggio(a1)
iss.aggiungi_equipaggio(a2)

# operazioni
m1.avanza_ore(520)
m1.aggiorna_sistema_vita(18, 28, 101.3)
a1.esegui_eva(6)

# visita modulo (ASSOCIAZIONE)
iss.astronauta_visita_modulo(a1, m1)

# report
iss.mostra_stazione()
iss.report_sistemi_vita()

# verifica aggregazione
del iss
print(a1)  # esiste ancora!       
    
    
        
        
