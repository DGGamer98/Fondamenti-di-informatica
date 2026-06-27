class eta_non_idonea(Exception):
    pass
class matricola_non_valida(Exception):
    pass

class Persona():
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.__eta = eta

    @property
    def eta(self):
        return self.__eta
    @eta.setter
    def eta(self, eta):
        if eta >= 18:
            print("[LOG] maggiorenne")
        else:
            raise eta_non_idonea("La persona è minorenne") 


#Eredito Persona con due classi figlie
class Cliente(Persona):
    def __init__(self, nome, cognome, eta):
        super().__init__(nome, cognome, eta)

    def __str__(self):
        return f"Cliente --> | nome: {self.nome} | cognome: {self.cognome} | eta: {self.eta}"

class Cameriere(Persona):
    def __init__(self, nome, cognome, eta, matricola):
        super().__init__(nome, cognome, eta)

        self.__matricola = matricola

    @property
    def matricola(self):
        return self.__matricola
    
    @matricola.setter
    def matricola(self, matricola):
        if matricola.isdigit and matricola.isaplha():
            print("[LOG] matricola valida")
        else:
            raise matricola_non_valida("La matricola deve contenere numeri e caratteri")

    def __str__(self):
        return f"Cameriere --> | nome: {self.nome} | cognome: {self.cognome} | eta: {self.eta} | matricola: {self.matricola} "
       


