import unittest

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
            print("[LOG] maggiorenne")
            return True
        else:
            return False
        
    def __str__(self):
        return f"Persona --> | Nome: {self.nome} | Cognome {self.cognome} | Eta: {self.eta}"

#Classe --> verra inizializzata ogni volta che verrà inizializzata l'entità Studente
class librettoVoti():
    def __init__(self):
        self.voto = []
        self.media = 0
        
    def media_voti(self):
        #imposto le variabili per il calcolo
        counter = 0
        somma = 0
        
        for x in self.voto:
            counter+=1
            somma+=x
        
        self.media = somma/counter
        return self.media
    
    def __str__(self):
        return f"libretto --> | voti: {self.voto} | media: {self.media}"
        

#Eredita dalla super class Persona
class Studente(Persona):
    def __init__(self, nome, cognome, eta, matricola, indirizzo,):
        super().__init__(nome, cognome, eta)
        
        self.matricola = matricola
        self.indirizzo = indirizzo
        self.libretto_voto = librettoVoti() #Relazione di composizione
        self.lista_corsi = [] #Relazione di aggregazzione con classe Corsi
        
    def controllo_matricola(self):
        maiuscolo = 0
        minuscolo = 0
        
        for char in self.matricola:
            #controllo stinga alfanumerica
            if char.isalnum():
                print("[LOG] la matricola contiene numeri e caratteri")
            #controllo caratteri maiuscoli e minuscoli
            if char.isupper():
                maiuscolo+=1
            elif char.islower():
                minuscolo+=1
              
    def conteggio_numeri_lettere(self):
        letter = 0
        number = 0
        for x in self.matricola:
            if x.isdigit():
                number+=1
            elif x.isalpha():
                letter+=1
                
    def add_corso(self, corso): #Relazione di associazione + aggregazione
        #Prima controllo se i corsi sono meno di tre
        if len(self.add_corso) > 3:
            print("[LOG] massimo 3 corsi puoi seguire")
            return False
        
        self.lista_corsi.append(corso)
        return f"Iscrizione corso completata !"
    
    def __str__(self):
        corsi = " ".join(self.lista_corsi)
        return f"Studente ---> | Nome: {self.nome} | Cognome: {self.cognome} | eta {self.eta} | matricola {self.matricola} | libretto {self.libretto_voto} | corsi {corsi} "
    
#Eredita dalla super class Persona
class Professore(Persona):
    def __init__(self, nome, cognome, eta, matricola_prof):
        super().__init__(nome, cognome, eta)
        
        self.matricola_prof = matricola_prof
        
    def controllo_matricola_prof(self):
        maiuscolo = 0
        minuscolo = 0
        
        for char in self.matricola_prof:
            #controllo stinga alfanumerica
            if char.isalnum():
                print("[LOG] la matricola contiene numeri e caratteri")
            #controllo caratteri maiuscoli e minuscoli
            if char.isupper():
                maiuscolo+=1
            elif char.islower():
                minuscolo+=1
        
    def conteggio_numeri_lettere(self):
        letter = 0
        number = 0
        for x in self.matricola_prof:
            if x.isdigit():
                number+=1
            elif x.isalpha():
                letter+=1
                
    def __str__(self):
        return f"Professore ---> | nome: {self.nome} | cognome: {self.cognome} | eta: {self.eta} | matricola_prof {self.matricola_prof}"

#usiamo l'aggregazione per aggregare le entità Professore e Studente            
class corso():
    def __init__(self, nome):
        self.nome = nome
        self.list_studenti = []
        self.list_professori = []
        
    #Avviene l'associazione + aggregazione
    def iscrizione_corso(self, studente):
        self.list_studenti.append(studente)
        return f"Studente iscritto con successo"
    
    def iscrivi_professore(self, professore):
        self.list_professori.append(professore)
        return f"Docente iscritto"
    
    



#Questa entità gestirà tutto !!
class Università():
    
        
    
    