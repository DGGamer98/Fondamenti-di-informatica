class ContoBancario:
    def __init__(self, saldo):
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
c = ContoBancario(1000)
print(c.saldo)
c.saldo = 500 #Attribute error