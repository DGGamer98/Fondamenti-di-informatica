'''Traccia: Sistema Concessionaria Auto
Contesto: Progetta un sistema per gestire una concessionaria con auto, clienti e venditori.
Entità del sistema:

Una Persona come classe base. Un Cliente che acquista o noleggia auto. Un Venditore che gestisce le vendite. Un'Auto con una sua scheda tecnica. Una Concessionaria che coordina tutto.
Relazioni richieste:

Almeno una ereditarietà
Almeno una composizione
Almeno una aggregazione
Almeno una associazione

Vincoli semantici con @property:

L'età del cliente deve essere tra 18 e 100
Il prezzo dell'auto deve essere maggiore di 0
Un cliente può prenotare massimo 2 test drive contemporaneamente

Eccezioni da gestire:

Auto non disponibile
Auto non trovata
Età non valida
Troppi test drive prenotati
Concessionaria al completo

Decorator richiesti:

Uno di log con timestamp
Uno che controlla che l'auto sia disponibile prima del test drive

Il sistema deve permettere di:

Aggiungere auto e clienti alla concessionaria
Prenotare un test drive
Vendere un'auto
Cercare un'auto per modello
Stampare il report completo

Test con unittest:

test_eta_valida — assertEqual
test_eta_non_valida — assertRaises
test_test_drive_ok — assertTrue
test_auto_non_disponibile — assertRaises
test_troppi_test_drive — assertRaisesRegex'''
import unittest

class auto_non_disponibile(Exception):
    pass
class Auto_non_trovata(Exception):
    pass
class Eta_non_valida(Exception):
    pass
class Conessionaria_al_completo(Exception):
    pass


class Persona():
    def __init__(self, nome, cognome, eta):
        self.__nome = nome
        self.__cognome = cognome
        self.__eta = eta

    @property
    def nome(self):
        return self.__nome
    @property
    def cognome(self):
        return self.__cognome
    @property
    def eta(self):
        return self.__eta
    
    @eta.setter
    def eta(self, eta):
        if eta >= 18:
            self.__eta = eta
            return True
        else:
            raise Eta_non_valida("La persona è minorenne")
        
class Scheda_Tenica():
    def __init__(self, EURO, GPL, BOLLO_PAGATO, Assicurazione):
        self.__EURO = EURO
        self.__GPL = GPL
        self.__BOLLO_PAGATO = BOLLO_PAGATO
        self.__Assicurazione = Assicurazione

    #sola lettura
    @property
    def euro(self):
        return self.__EURO
    @property
    def gpl(self):
        return self.__GPL
    @property
    def bollo_pagato(self): 
        return self.__BOLLO_PAGATO
    @property
    def assicurazione(self):
        return self.__Assicurazione
    
    #scrittura dei attributi di istanza --> cambiano nel tempo
    @bollo_pagato.setter
    def bollo_pagato(self, new_pagamento):
        if new_pagamento == 0:
            raise ValueError ("Bollo auto non pagato")
        elif new_pagamento > 0:
            print("[LOG] bollo auto pagato")
            return True
        
    @assicurazione.setter
    def assicurazione(self, new_assicurazione):
        if new_assicurazione == 0:
            raise ValueError ("Bollo auto non pagato")
        elif new_assicurazione > 0:
            print("[LOG] bollo auto pagato")
            return True
        
    def __str__(self):
        return f"Scheda Auto --> | EURO: {self.euro} | GPL: {self.gpl} | BOLLO_PAGATO: {self.bollo_pagato} | Assicurazione: {self.assicurazione}"
        
class Auto():
    def __init__(self, modello, marca, anno_matricolazione, costo, EURO, GPL, BOLLO_PAGATO, Assicurazione):
        self.modello = modello
        self.marca = marca
        self.anno_matricolazione = anno_matricolazione
        self.costo = costo
        self.scheda_tecnica = Scheda_Tenica(EURO, GPL, BOLLO_PAGATO, Assicurazione) #Composizione

    def __str__(self):
        return f"Auto --> | modello: {self.modello} | marca: {self.marca} | anno_matricolazione: {self.anno_matricolazione} | costo: {self.costo} |scheda_tecnica: {self.scheda_tecnica}"

class Cliente(Persona):
    def __init__(self, nome, cognome, eta):
        super().__init__(nome, cognome, eta)

        #per reperire le informazioni nel tempo
        self.aquisti = []
        self.noleggio = []  
    
    def noleggio_auto(self, auto, id):
        veicolo = {id: auto}
        self.noleggio.append(veicolo)
        print("[LOG] veicolo noleggiato")
        return self.noleggio

    def acquista_auto(self, auto, id):
        veicolo = {id: auto}
        self.aquisti.append(veicolo)
        print("[LOG] veicolo acquistato")
        return self.aquisti
    
    def __str__(self):
        return f"Cliente --> | Nome: {self.nome} | Cognome: {self.cognome} | eta: {self.eta}"


class Venditore(Persona):
    def __init__(self, nome, cognome, eta):
        super().__init__(nome, cognome, eta)

        self.vendite_auto = {}
    
    def gestione_vendite(self, Cliente, Auto):
        self.vendite_auto[Cliente] = Auto
        print("[LOG] Auto venduta")
        return self.vendite_auto
    
    def __str__(self):
        return f"Venditore --> | Nome: {self.nome} | Cognome: {self.cognome} | eta: {self.eta}"
    

# cliente1 = Cliente("Davide","Gatta",23)
# venditore = Venditore("Mario","Rossi", 35)
# auto = Auto("Citroen C-3", "Citroen", 2021, 3200, "EURO 5", "No", "Si", "Cattolica")

# print(cliente1)
# print(venditore)
# print(auto)

class testCode(unittest.TestCase):
    #metodo per creare i nostri oggetti
    def setUp(self):
        self.cliente1 = Cliente("Davide","Gatta",23)
        self.venditore = Venditore("Mario","Rossi", 35)
        self.auto = Auto("Citroen C-3", "Citroen", 2021, 3200, "EURO 5", "No", "Si", "Cattolica")
        self.auto2 = Auto("Golf 8", "Volkswagen", 2022, 15000, "EURO 6", "No", "Si", "UnipolSai")

    def test_acquisto(self):
        self.assertTrue(self.cliente1.acquista_auto(self.auto, 1))
    def test_noleggio(self):
        self.assertTrue(self.cliente1.noleggio_auto(self.auto2, 1))

    def test_vendita(self):
        self.assertTrue(self.venditore.gestione_vendite(self.cliente1, self.auto))
        

        
if __name__ == "__main__":
    unittest.main()