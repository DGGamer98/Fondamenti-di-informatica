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
        if matricola.isalnum():
            print("[LOG] matricola valida")
        else:
            raise matricola_non_valida("La matricola deve contenere numeri e caratteri")
        
    def __str__(self):
        return f"Cameriere --> | nome: {self.nome} | cognome: {self.cognome} | eta: {self.eta} | matricola: {self.matricola} "

class Ricevuta():
    def __init__(self, importo, iva, coperto):
        self.importo = importo
        self.iva = iva
        self.coperto = coperto

    def __str__(self):
        return f"Ricevuta --> |importo {self.importo} |iva: {self.iva} |coperto: {self.coperto}"

class Ordine():
    def __init__(self, nome_piatto, importo, iva, coperto):
        self.nome_piatto = nome_piatto
        self.ricevuta = Ricevuta(importo, iva, coperto) #Relazione di composizione

    def __str__(self):
        return f"Ordine --> | nome_piatto {self.nome_piatto} | {self.ricevuta}"
    
class Ristorante():
    def __init__(self, nome, via):
        self.nome = nome
        self.via = via
        self.prenotati = [] #massimo 6 clienti
        self.Ordini = [] #relazione di aggrefazione
    
    def prenotazioni(self, id, Cliente):
        if len(self.prenotati) > 6:
            print("Non è possibile prenotare")
            return False
        
        cliente = {id, str(Cliente)}
        self.prenotati.append(cliente)
        print("[LOG] cliente prenotato")

    def mostra_clienti(self):
        for cliente in self.prenotati:
            print(cliente)

        #Metodo per ordinare il piatto
    def ordine_piatto(self, Cliente, Ordine): #Relazione di associazione
        comanda = {Cliente,Ordine}
        self.Ordini.append(comanda)
        return f"il cliente {Cliente} ha ordinato il piatto {Ordine}"


#Istanzio gli oggetti
cliente1 = Cliente("Davide","Gatta", 23)
cameriere1 = Cameriere("Anies","abdul", 19, "32604")
ordine1 = Ordine("Carbonara", 10, 2, 0)
bottega = Ristorante("parolaccia","Trastevere")

cameriere1.matricola = "alfs32604"
cameriere1.eta = 16

#Uso le relazioni
bottega.prenotazioni(1, cliente1)
bottega.mostra_clienti()

print(bottega.ordine_piatto(cliente1, ordine1))
