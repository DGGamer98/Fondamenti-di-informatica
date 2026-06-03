class TermostatoIntelligente():
    def __init__(self, temperatura_targe):
        self.__temperatura_target = temperatura_targe
        self.__acceso = "spento"
        self.__modalita = "automatico"
        
    
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
            
    #Logica di business
    def accendi(self):
        self.__acceso = "Acceso"
        return
        
    def spegni(self):
        self.__acceso = "Spento"
        return 
    
    def imposta_temperatura(self, nuova_temperatura):
        if int(nuova_temperatura):
            self.lettura_valore_temperatura = nuova_temperatura
        else:
            raise ValueError ("Formato temperatua non valido")
        
    def imposta_modalita(self, nuova_modalita="automatico"):
        self.lettura_valore_modalita = nuova_modalita
        
    
    '''TODO Davide
    Requisiti aggiuntivi:
        - se la temperatura o la modalità non sono valide, stampare un messaggio di errore e non modificare lo stato dell’oggetto;
        - il termostato deve partire spento;
        - la modalità iniziale deve essere "automatico"
        '''
        

termostato = TermostatoIntelligente(25)
print(termostato.lettura_valore_accesso)    # → Spento
print(termostato.lettura_valore_modalita)   # → automatico
print(termostato.lettura_valore_temperatura)# → 20


termostato.accendi()
print(termostato.lettura_valore_accesso)

# imposta temperatura valida
try:
    termostato.imposta_temperatura(25) 
    print(termostato.lettura_valore_temperatura)  # → 25
except ValueError as e:
    print(e)

# imposta temperatura non valida
try:
    termostato.imposta_temperatura(50)     
except ValueError as e:
    print(e)

# imposta modalità valida
try:
    termostato.imposta_modalita("riscaldamento")  
    print(termostato.lettura_valore_modalita)
except ValueError as e:
    print(e)

# imposta modalità non valida
try:
    termostato.imposta_modalita("ventilazione")   
except ValueError as e:
    print(e)

# spegni
termostato.spegni()
print(termostato.lettura_valore_accesso) 

