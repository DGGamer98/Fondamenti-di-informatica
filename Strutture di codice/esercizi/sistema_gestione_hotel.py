'''TODO Traccia task esercizio ESAME

Traccia: Sistema di gestione hotel
Contesto: Devi progettare un sistema per la gestione di un hotel che gestisce camere, ospiti e prenotazioni.

Entità del sistema:
Un Ospite con nome, età e documento d'identità. 
Una Camera con numero, tipo e prezzo per notte. 
Una Prenotazione che collega un ospite a una camera con date di check-in e check-out. 
Un Hotel che coordina tutto.

Relazioni richieste:

Almeno una ereditarietà
Almeno una composizione
Almeno una aggregazione
Almeno una associazione

Vincoli semantici con @property:

L'età dell'ospite deve essere tra 18 e 100
Il prezzo per notte deve essere maggiore di 0
Il tipo di camera deve essere uno tra: "singola", "doppia", "suite"
Il numero di camera deve essere maggiore di 0

Eccezioni da gestire:

Camera già occupata (customizzato)
Ospite già registrato (customizzato)
Date non valide (check-out prima di check-in)
Documento d'identità non valido (meno di 5 caratteri)
Hotel al completo (customizzato)

Decorator richiesti:

Uno di log con timestamp
Uno che controlla che la camera sia disponibile prima di prenotare

Il sistema deve permettere di:

Registrare un ospite
Prenotare una camera
Fare il check-in e check-out
Stampare il report completo dell'hotel con camere libere e occupate'''

#Eccezzioni Customizzate
class Camera_gia_occupata(Exception):
    pass
class Ospite_già_registrati(Exception):
    pass
class Hotel_al_completo(Exception):
    pass

#Decorator
def log_function(function):
    def wrapper(*args, **kwargs):
        print(f"[LOG] operazioni in corso {function.__name__}")
        result = function(*args, **kwargs)
        print("[LOG] operazione terminata")
        return result
    return wrapper

def check_camera_disponibile(func):
    def wrapper(self, Camera, Ospite):
        if Camera in self.camere_prenotate:
            raise Camera_gia_occupata("[Error] la camera è già occupata")
        
        if self.camere_disponibili <= 0:
            raise Hotel_al_completo("[Error] l'hotel è al completo")
                
        return func(self, Camera, Ospite)
    return wrapper

class Hotel():
    def __init__(self, nomeHotel, indirizzo, numero_camere):
        self.nomeHotel = nomeHotel
        self.indirizzo = indirizzo
        self.numero_camere = numero_camere

    def __str__(self):
        return f"Dettagli hotel: | nome hotel: {self.nomeHotel} | indirizzo hotel: {self.indirizzo} | numero camere totali {self.numero_camere} |"

class Ospite():
    def __init__(self, nome, eta, numero_documento):
        self.__nome = nome
        self.__eta = eta
        self.__numero_documento = numero_documento

    #metodo GETTER
    @property 
    def nome(self):
        return self.__nome
    @property
    def eta(self):
        return self.__eta
    @property
    def numero_documento(self):
        return self.__numero_documento
    
    #SETTER
    @eta.setter
    def eta(self, eta):
        #Logica per controllare se il ragazzo è maggiorenne o no
        if eta >= 18:
            self.__eta = eta
            print("[LOG] ragazzo maggiorenne")
        else:
            raise ValueError("[Error] Il ragazzo è minorenne")
    
    def __str__(self):
        return f"| Nome: {self.nome} | Età: {self.eta} | numero documento: {self.numero_documento}"
    
class Camera():
    def __init__(self, numero, prezzo_notte):
        self.__numero = numero
        self.tipo = ["singolo","matrimoniale","suite"]
        self.__prezzo_notte = prezzo_notte
        
    @property
    def numero(self):
        return self.__numero
    
    @property
    def prezzo_notte(self):
        return self.__prezzo_notte
    
    @numero.setter
    def numero(self, numero_camera):
        if numero_camera > 0:
            self.__numero = numero_camera
            print("[LOG] prezzo ok")
        elif numero_camera <= 0:
            raise ValueError ("[Error] numero camera non può essere minore 0 uguale a 0")
            
    @prezzo_notte.setter
    def prezzo_notte(self, prezzo):
        if prezzo > 0:
            self.__prezzo_notte = prezzo
            print("[LOG] prezzo ok")
        elif prezzo <= 0:
            raise ValueError ("[Error] il prezzo non può essere inferiore o uguale a 0")
            
    def __str__(self):
        return f"Camera: | numero: {self.__numero} | tipo: {"singolo"} | prezzo notte:  {self.__prezzo_notte}"
@log_function
class Prenotazione():
    def __init__(self, camera, ospite, data_checkin, data_checkout):
        self.camera = camera
        self.ospite = ospite
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.camere_disponibili = 300
        self.camere_prenotate = {}
        
    @check_camera_disponibile
    def prenota_stanza(self, Camera, Ospite):
        self.camere_prenotate[Camera] = Ospite
        self.camere_disponibili -= 1
        print(f"[LOG] camera aggiunta")
 
    def __str__(self):
        return f"Prenotazione: -> {self.camera} | data_checkin: {self.data_checkin} | data checkout: {self.data_checkout} | camere disponibili: {self.camere_disponibili} | Dati ospite: {self.ospite}"

'''ZONA DI TEST PER L'ALGORITMO DEL CODICE PYTHON'''

camera1 = Camera(1213, 30)

ospite1 = Ospite("Davide",23,"BA23cz90")
ospite2 = Ospite("Luca",25,"CZ23mbrt")

prenotazione1 = Prenotazione(camera1, ospite2, 10, 12)

ospite1.eta = 18
#print(ospite1)

#prenotazione ospite 1
try:
    prenotazione1.prenota_stanza(camera1, ospite1)
    print(prenotazione1)
except ValueError as e:
    print(f"La camera è già occupata {e}")
finally:
    print("Blocco try")

#Prenotazine ospite2
try:
    prenotazione1.prenota_stanza(camera1, ospite2)
    print(prenotazione1)
except ValueError as e:
    print(f"La camera è già occupata {e}")
finally:
    print("Blocco try")
    

