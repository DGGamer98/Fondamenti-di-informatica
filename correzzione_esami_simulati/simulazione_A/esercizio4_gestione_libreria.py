
class LibroNonDisponibile(Exception):
    pass
class TroppiLibriInPrestito(Exception):
    pass
class EtaNonValida(Exception):
    pass
class MatricolaNonValida(Exception):
    pass
class Lavoratore_già_esistente(Exception):
    pass
class Cliente_già_esistente(Exception):
    pass

class Persona():
    def __init__(self, nome, eta):
        self.__nome = nome
        self.__eta = eta

    @property
    def nome(self):
        return self.__nome
    @property
    def eta(self):
        return self.__eta

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @eta.setter
    def eta(self, eta):
        self.__eta = eta
        if eta > 18:
            print("maggiorenne")
        else:
            raise EtaNonValida("Eta non valida")

    def __str__(self):
        return f"Nome: {self.nome} eta: {self.eta}"


class Libro():
    def __init__(self, titolo, autore, disponibile):
        self.titolo = titolo
        self.autore = autore
        self.disponibile = disponibile

    def __str__(self):
        return f"Libro ---> | Titolo: {self.titolo} | Autore: {self.autore} | disponibile: {self.disponibile}"

class Cliente(Persona):
    def __init__(self, nome, eta, titolo, autore, disponibile):
        super().__init__(nome, eta)
        self.lista_libri = []
        self.scheda_prestiti = Libro(titolo, autore, disponibile)

    def controllo_lista(self):
        if len(self.lista_libri) > 3:
            raise TroppiLibriInPrestito("Troppi libri massimo 3")

    def __str__(self):
        return f"|Nome: {self.nome} |eta: {self.eta} |titolo: {self.scheda_prestiti.titolo}|autore: {self.scheda_prestiti.autore} |disponibile: {self.scheda_prestiti.disponibile}"

        
class Bibliotecari(Persona):
    def __init__(self, nome, eta, matricola):
        super().__init__(nome, eta)

        self.matricola = matricola

    def timbratura_matricola(self):
        timbro = input("Inserisci matricola: ")

        if self.matricola == timbro:
            print("Timbro effettuato")
        else:
            raise MatricolaNonValida("Matricola non valida")

    def __str__(self):
        return f"|Nome: {self.nome} |eta: {self.eta} |Matricola: {self.matricola}"

class Biblioteca():
    def __init__(self):
        self.list_clienti = []
        self.list_lavoratori = []
        self.libri = []

    def mew_lavoratore(self, id, Bibliotecari):
        controlloId = int(input("Cerca id"))
        if controlloId in self.list_lavoratori:
            raise Lavoratore_già_esistente("Lavoratore già presente")
        
        patternDict = {id:str(Bibliotecari)}
        self.list_lavoratori.append(patternDict)

    def new_cliente(self, id, Cliente):
        controlloId = int(input("Cerca id"))
        if Cliente in self.list_clienti:
            raise Cliente_già_esistente("Cliente già esistente")

        patternDict = {id:str(Cliente)}
        self.list_clienti.append(patternDict)

    def presta_libro():
        #TODO Davide finire la funzione per prestare libro

    def stampa_clienti(self):
        for x in self.list_clienti:
            print(x)

    def stampa_lavoratori(self):
        for x in self.list_lavoratori:
            print(x)

libro = Libro("Divina commedia","Dante alighieri", True)
cliente = Cliente("Davide","Gatta","Divina commedia","Dante alighieri", True)
bibliotecaria = Bibliotecari("Alberto",45,"23Alfa")


biblioteca = Biblioteca()

biblioteca.new_cliente(1, cliente)
biblioteca.mew_lavoratore(1, bibliotecaria)

biblioteca.stampa_clienti()
biblioteca.stampa_lavoratori()



    