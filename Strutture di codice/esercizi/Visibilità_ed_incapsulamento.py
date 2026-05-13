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
    def set_valore_temperatura(self):
        if self.lettura_valore_temperatura >= 10 and self.lettura_valore_temperatura <= 30:
            print("[LOG] temperatura entro i limiti")
        else:
            print("[ERROR] temperatura al di fuori dei limiti")
        #TODO Controllare la logica
        self.__temperatura_target = self.set_valore_temperatura
    
        
    
    '''TODO -Impostazione vincoli semantici la temperatura target deve essere compresa tra 10 e 30 gradi;
            
            -la modalità deve essere una tra:
                -"riscaldamento"
                -"raffreddamento"
                -"automatico"
'''


#Regione per i test
termostato = TermostatoIntelligente(30, "Spento", "riscaldamento")


print(termostato.lettura_valore_temperatura)
print(termostato.lettura_valore_modalita)
print(termostato.lettura_valore_accesso)

