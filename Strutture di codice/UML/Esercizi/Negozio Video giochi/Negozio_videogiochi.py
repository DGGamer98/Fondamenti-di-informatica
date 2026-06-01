'''Traccia: Sistema Negozio di Videogiochi
Contesto: Progetta un sistema per gestire un negozio di videogiochi con giochi, clienti e commessi.
Entità del sistema:
Una Persona come classe base. Un Cliente che acquista e noleggia giochi. Un Commesso che gestisce le vendite. Un Videogioco con una sua scheda tecnica. Un Negozio che coordina tutto.
Relazioni richieste:

Almeno una ereditarietà
Almeno una composizione
Almeno una aggregazione
Almeno una associazione

Vincoli semantici con @property:

L'età deve essere tra 10 e 99
Il prezzo del videogioco deve essere maggiore di 0
Un cliente può noleggiare massimo 3 giochi contemporaneamente

Eccezioni da gestire:

Gioco non disponibile
Gioco non trovato
Età non valida
Troppi noleggi attivi
Negozio al completo

Il sistema deve permettere di:

Aggiungere videogiochi e clienti al negozio
Noleggiare un videogioco
Restituire un videogioco
Cercare un gioco per titolo
Stampare il report completo del negozio

Test con unittest:

test_eta_valida — assertEqual
test_eta_non_valida — assertRaises
test_noleggio_ok — assertTrue
test_gioco_non_disponibile — assertRaises
test_troppi_noleggi — assertRaisesRegex

'''

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
        
    #setter + logica per eta
    @eta.setter
    def eta(self, eta):
        if eta >= 10 and eta <= 99:
           print("[LOG] ragazzo può comprare i videogiochi")
        else:
            raise ValueError ("Il ragazzo è troppo piccolo o troppo anziano")
        
        if eta >= 18:
            print("[LOG] il ragazzo può prendere i peghi 18") 
            
    def __str__(self):
        return f"Nome: {self.__nome} Cognome: {self.__cognome} eta: {self.__eta}"
    
class Cliente(Persona):
    def __init__(self, nome, cognome, eta):
        super().__init__(nome, cognome, eta)
        
    #TODO Finire i due metodi --> associazione di videogioco
    def Aquista(self, video_gioco):
        pass
    
    def Noleggia(self, video_gioco):
        pass

class Commesso(Persona):
    def __init__(self, nome, cognome, eta):
        super().__init__(nome, cognome, eta)
    #TODO Finire di creare la classe gestione vendite --> associa Cliente e viedogioco
    def gestioneVendite(self, Cliente, video_gioco):
        pass
    
#TODO creare la classe video gioco (Seguire lo schema UML)