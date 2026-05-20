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

Camera già occupata
Ospite già registrato
Date non valide (check-out prima di check-in)
Documento d'identità non valido (meno di 5 caratteri)
Hotel al completo

Decorator richiesti:

Uno di log con timestamp
Uno che controlla che la camera sia disponibile prima di prenotare

Il sistema deve permettere di:

Registrare un ospite
Prenotare una camera
Fare il check-in e check-out
Stampare il report completo dell'hotel con camere libere e occupate'''

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
            print("[LOG] ragazzo maggiorenne")
            self.__eta = eta
        else:
            raise ValueError("[Error] Il ragazzo è minorenne")
    
    def __str__(self):
        return f"| Nome: {self.nome} | Età: {self.eta} | numero documento: {self.numero_documento}"
    
class Camera():
    def __init__(self, numero, prezzo_notte):
        self.numero = numero
        self.tipo = ["singolo","matrimoniale","suite"]
        self.prezzo_notte = prezzo_notte
    
class Prenotazione(Camera):
    def __init__(self, numero, prezzo_notte, data_checkin, data_checkout):
        super().__init__(numero, prezzo_notte)
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.camere_disponibili = 300
        self.camere_prenotate = {}

    def prenota_stanza(self, Camera, Ospite):
        if self.data_checkout > self.data_checkin:
            raise ValueError ("il checkout non può essere maggiore di data checkin")
        elif self.data_checkin == self.data_checkout:
            raise ValueError("il checkoin non può essere uguale al checkout")
        
        self.camere_prenotate.update(Camera,Ospite)
        print(f"[LOG] La camera {Camera} è stata prenotata per {Ospite}")
        

'''ZONA DI TEST PER L'ALGORITMO DEL CODICE PYTHON'''

ospite1 = Ospite("Davide",23,"BA23cz90")

# ospite1.nome = "Davide"
#ospite1.numero_documento = "BA23cz90"
ospite1.eta = 18
print(ospite1)

#TODO Davide: Testare il metodo delle prenotazioni e decrementare il numero delle camere disponibili


