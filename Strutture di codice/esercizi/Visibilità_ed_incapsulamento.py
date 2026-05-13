class TermostatoIntelligente():
    def __init__(self, temperatura_target, acceso, modalita):
        self.__temperatura_target = temperatura_target
        self.__acceso = acceso
        self.__modalita = modalita
        
    
    #accesso in sola lettura
    @property
    def lettura_valore_temperatura(self):
        return self.__temperatura_target 
    
    @property
    def lettura_valore_accesso(self):
        return self.__acceso
    
    @property
    def lettura_valore_modalita(self):
        return self.__modalita
    
    
    @lettura_valore_temperatura.setter
    def lettura_valore_temperatura(self, temperatura_target):
        if temperatura_target >= 10 and temperatura_target <= 30:
            print("[LOG] temperatura entro i limiti")
        else:
            raise ValueError("[ERROR] temperatura fuori dai limiti, deve essere compresa tra 10 e 30 gradi")
        self.__temperatura_target = temperatura_target #setter intercetta quando scriviamo
    
    @lettura_valore_modalita.setter
    def lettura_valore_modalita(self, modalita):
        listaMod = ["riscaldamento","raffreddamento","automatico"]
        
        #controllo se modalita non esiste nella lista
        if modalita not in listaMod:
            raise ValueError ("[ERROR] modalità non presente")
        else:
            self.__modalita = modalita
            print(f"[LOG] Hai scelto {modalita}")



#Regione per i test
termostato = TermostatoIntelligente(30, "Spento", "riscaldamento")

termostato.lettura_valore_temperatura=25 #uso il setter
print(termostato.lettura_valore_temperatura) #uso il getter

termostato.lettura_valore_modalita = "riscaldamento"
print(termostato.lettura_valore_modalita)

