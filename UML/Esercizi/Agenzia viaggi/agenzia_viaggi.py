'''
📋 Traccia: Sistema Agenzia Viaggi
Contesto: Progetta un sistema per gestire un'agenzia viaggi con destinazioni, clienti e agenti.
Entità del sistema:
Una Persona come classe base. Un Cliente che prenota viaggi. Un Agente che gestisce le prenotazioni. Una Destinazione con una sua scheda informativa. Una Agenzia che coordina tutto.
Relazioni richieste:

Almeno una ereditarietà
Almeno una composizione
Almeno una aggregazione
Almeno una associazione
Almeno una dipendenza

Vincoli semantici con @property:

L'età deve essere tra 18 e 90
Il prezzo del viaggio deve essere maggiore di 0
Un cliente può prenotare massimo 3 viaggi contemporaneamente

Eccezioni da gestire:

Destinazione non disponibile
Destinazione non trovata
Età non valida
Troppi viaggi prenotati
Agenzia al completo

Decorator richiesti:

Uno di log con timestamp
Uno che controlla che la destinazione sia disponibile

Il sistema deve permettere di:

Aggiungere destinazioni e clienti all'agenzia
Prenotare un viaggio
Cancellare una prenotazione
Cercare una destinazione per nome
Stampare il report completo

Test con unittest:

test_eta_valida — assertEqual
test_eta_non_valida — assertRaises
test_prenotazione_ok — assertTrue
test_destinazione_non_disponibile — assertRaises
test_troppi_viaggi — assertRaisesRegex
'''

import unittest

class Persona():
    def __init__(self, nome, cognome, eta):
        self.__nome = nome
        self.__cognome = cognome
        self.__eta = eta

    #incapsulamento

    @property
    def nome(self):
        return self.__nome
    @property
    def cognome(self):
        return self.__cognome
    @property
    def eta(self):
        return self.__eta
    
    #il setter assrnga il nuovo valore se True, poi richiama la property.
    @eta.setter
    def eta(self, eta):
        if eta >= 18:
            print("[LOG] persona maggiorenne")
            self.__eta = eta
        else:
            print("[Errore] persona minorenne") #Aggiungere l'eccezzione
            return False
        
class Cliente(Persona):
    def __init__(self, nome, cognome, eta, codice_cliente):
        super().__init__(nome, cognome, eta)

        self.__codice_cliente = codice_cliente

    @property
    def codice_cliente(self):
        return self.codice_cliente
    
    @codice_cliente.setter
    def codice_cliente(self, new_codice):
        #controllo se la stringa contiene numeri lettere 
        if new_codice.isalnum():
            print("[LOG] il codice contiene numeri e lettere")
        else:
            print("[Error] codice non valido") #Sostituire con eccezione

        #Secondo modo
        counter_letter = 0
        counter_num = 0
        for x in new_codice:
            if x.isdigit():
                counter_num+=1
            elif x.isalpha():
                counter_letter+=1

    def controllo_codice_corrente(self):
        #controllo se la stringa contiene numeri lettere 
        if self.codice_cliente.isalnum():
            print("[LOG] il codice contiene numeri e lettere")
        else:
            print("[Error] codice non valido") #Sostituire con eccezione

        #Secondo modo
        counter_letter = 0
        counter_num = 0
        for x in self.codice_cliente:
            if x.isdigit():
                counter_num+=1
            elif x.isalpha():
                counter_letter+=1
    
    def __str__(self):
        return f"Cliente ---> | nome: {self.nome} | cognome: {self.cognome} | eta: {self.eta} | codice cliente {self.codice_cliente}"

class Agente(Persona):
    def __init__(self, nome, cognome, eta, matricola):
        super().__init__(nome, cognome, eta)

        self.matricola = matricola

    #Metodo prenota viaggio --> associamo la classe Cliente, Destinazione

    def prenota_viaggi(self, cliente, destinazione): #Relazione di associazione
        myDict = {cliente, destinazione}
        print("[LOG] viaggio prenotato")
        return myDict
    
    def __str__(self):
        return f"Agente --> | nome: {self.nome} | cognome: {self.cognome} | eta: {self.eta} | matricola: {self.matricola}"
    
class Scheda_viaggio():
    def __init__(self, costo_totale, ore_viaggio, giorni_totali):
        self.costo_totale = costo_totale
        self.ore_viaggio = ore_viaggio
        self.giorni_totali = giorni_totali

    def __str__(self):
        return f"scheda_viaggio --> | costo totale: {self.costo_totale} euro | ore viaggio: {self.ore_viaggio} ore | giorni totali: {self.giorni_totali} giorni"
    

class Destinazione():
    def __init__(self, citta, paese, nome_hotel, costo_totale, ore_viaggio, giorni_totali):
        self.città = citta
        self.paese = paese
        self.nome_hotel = nome_hotel
        self.scheda_viaggio = Scheda_viaggio(costo_totale, ore_viaggio, giorni_totali) #scheda viaggio ---> Relazione di composizione

    def __str__(self):
        return f"Desinazione --> | città: {self.città} | paese: {self.paese} | nome hotel: {self.nome_hotel} | scheda viaggio: {self.scheda_viaggio}"
    
#Classe che orchestra tutto !!!

# class Agenzia():
#     def __init__(self, nome, indirizzo, partita_iva):
#         self.nome = nome
#         self.indirizzo = indirizzo
#         self.partita_iva = partita_iva

#         #liste per le relazioni di aggregazione
#         self.lista_clienti = []
#         self.lista_agenti = []
#         self.lista_viaggi = []

#     def insert_clienti(self, cliente):
#         self.lista_clienti.append(cliente)
#         print("[LOG] cliente aggiunto")

class test_software(unittest.TestCase):
    #prepariamo tutti gli oggetti
    def setUp(self):
        self.cliente = Cliente("Davide","Gatta",23,"Alfa32")
        self.agente = Agente("Mario","Rossi",30,"Tre32")
        self.destinazione = Destinazione("Parigi", "Francia", "easy_hotel", 223.4, 2.5, 10)
    
    def test_prenota_viaggio(self):
        self.assertTrue(self.agente.prenota_viaggi(self.cliente, self.destinazione))
    
    def test_eta_valida(self):
        self.assertTrue(self.cliente.eta >= 18)
    
    # def test_eta_non_valida(self):
    #     self.assertTrue(self.cliente.eta < 18)

    

    
if __name__ == "__main__":
    unittest.main()


        
    
        






    


    
