class Person:
    def __init__(self, nome="", cognome="", eta=0):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.utenti = [] 

    def insert_input(self):
        self.nome = input("Inserisci nome: ")
        self.cognome = input("Inserisci cognome: ")
        try:
            self.eta = int(input("Inserisci età: "))
        except ValueError:
            print("Errore: Inserisci un numero per l'età!")
            self.eta = 0

        print(f"Dati salvati: {self.nome} {self.cognome}, {self.eta} anni")


persona1 = Person() 
persona1.insert_input()