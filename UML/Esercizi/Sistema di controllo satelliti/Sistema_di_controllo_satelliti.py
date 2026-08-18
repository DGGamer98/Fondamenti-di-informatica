import unittest
import time
import os
from tqdm import tqdm

class SpazioException(Exception):
    pass
class CarburanteNonValido(SpazioException):
    pass
class StatoNonValido(SpazioException):
    pass
class SatelliteNonTrovato(SpazioException):
    pass
class CentroAlCompleto(SpazioException):
    pass


class componenteSpaziale:
    def __init__(self, nome, stato):
        self.__nome = nome
        self.__stato = stato 
        
    @property
    def nome(self):
        return self.__nome
    @property
    def stato(self):
        return self.__stato
    
    @nome.setter
    def nome(self, nome):
        if nome.isalnum():
            print("[LOG] nome corretto")
            self.__nome = nome
            return True
    
    @stato.setter
    def stato(self, stato):
        if stato == True:
            self.__stato = stato
            return True
        else:
            raise StatoNonValido("Stato non valido usare solo valori booleani True o False")

#Relazione di composizione in Satellite
class RegistroEventi():
    def __init__(self, timeStamp):
        self.lista_eventi = []
        self.timeStamp = timeStamp
    
#Classe figlia della super class componenteSpaziale
class Satellite(componenteSpaziale):
    def __init__(self, nome, stato, orbita, carburante, timeStamp):
        super().__init__(nome, stato)
        self.orbita = orbita
        self.carburante = carburante
        self.registroEventi = RegistroEventi(timeStamp) # relazione di composizione
        self.log = {timeStamp: self.registroEventi.lista_eventi}
        
    def check_carburante(self):
        if self.carburante == 0 :
            raise CarburanteNonValido("Carburante a secco")
        
        print("[LOG] carburante apposto")
    
    def aggiungi_evento(self, evento):
        self.registroEventi.lista_eventi.append(evento)
        print("[LOG] evento aggiunto")
    
    
    def __str__(self):
        return f"nome satellite: {self.nome} ---> | stato: {self.stato} | orbita: {self.orbita} | carburante: {self.carburante} | eventi: {self.log}"
        
#Classe figlia della super class componenteSpaziale       
class Sonda(componenteSpaziale):
    def __init__(self, nome, stato, destinazione, distanza_percorsa):
        super().__init__(nome, stato)
        self.destinazione = destinazione
        self.distanza_percorsa = distanza_percorsa
            
    def avanza(self, avanzamento):
        self.distanza_percorsa+=avanzamento
        return self.distanza_percorsa
    
    def __str__(self):
        return f"nome sonda: {self.nome} ---> | stato sonda: {self.stato} | destinazione: {self.destinazione} | distanza percorsa: {self.distanza_percorsa}"


class CentroControllo():
    def __init__(self):
        self.lista_satellite = [] #max 10
        self.lista_sonda = [] #max 10
        
    def aggiungi_satellite(self, id, satellite): #relazione di aggrazazione verranno salvate nelle liste
        if len(self.lista_satellite) >= 10:
            raise CentroAlCompleto("Massimo 10 satelliti gestiti")
        
        sat = {id:satellite}
        self.lista_satellite.append(sat)
        print("[LOG] satellite aggiunto")
    
    def aggiungi_sonda(self, sonda): #relazione di aggrazazione verranno salvate nelle liste
        if len(self.lista_sonda) >= 10:
            raise CentroAlCompleto("Massimo 10 sonde gestite")
        
        self.lista_sonda.append(sonda)
        print("[LOG] sonda aggiunto")
        
    def report_tecnico_satellite(self,  tecnico):
        idSatellite = int(input("> cerca per id: "))
        for satellite in self.lista_satellite:
            if idSatellite == satellite:
                print(satellite)
    
    def report_tecnico_sonda(self, tecnico):
        ispezioneSonda = input("nome Sonda: ")
        
        for Sonda in self.lista_sonda:
            if ispezioneSonda == Sonda:
                return f"Il tecnico {tecnico} ispeziona il {ispezioneSonda}" 
              
'''Testiamo i metodi con di test'''

class testCodice(unittest.TestCase):
    def setUp(self): 
            #istanza centroControllo
            self.centroControllo = CentroControllo()
            #istanze sonda per test
            self.sonde = [
                Sonda("vojager1", True, "Sconosciuta", 2.55e10),
                Sonda("voyager2", True, "Spazio Interstellare", 2.02e9),
                Sonda("new-horizons", True, "Fascia di Kuiper", 8.8e8),
                Sonda("pioneer10", False, "Toro", 1.9e9),
                Sonda("parker-solar-probe", True, "Corona Solare", 1.5e8),
                Sonda("juno", True, "Orbitante attorno a Giove", 7.1e8),
                Sonda("cassini", False, "Atmosfera di Saturno", 1.4e9),
                Sonda("bepicolombo", True, "In transito verso Mercurio", 1.1e8),
                Sonda("rosetta", False, "Cometa 67P", 5.1e8),
                Sonda("juicy-juice", True, "In transito verso le lune di Giove", 6.2e8),
                Sonda("venera7", False, "Superficie di Venere", 1.08e8),
                Sonda("perseverance-descent-stage", False, "Superficie di Marte", 2.25e8),
            ]

            #istanze satellite per test
            self.satelliti = [
                Satellite("cosmo-skymed", True, "LEO", 50, "10/02/2026"),
                Satellite("sentinel-1a", True, "SSO", 2300, "03/04/2014"),
                Satellite("hubble", True, "LEO", 11110, "24/04/1990"),
                Satellite("galileo-foc1", True, "MEO", 700, "24/05/2016"),
                Satellite("meteosat-11", True, "GEO", 2000, "15/07/2015"),
                Satellite("james-webb", True, "L2", 6200, "25/12/2021"),
                Satellite("envisat", False, "SSO", 8211, "01/03/2002"),
                Satellite("starlink-3011", True, "LEO", 260, "12/05/2022"),
                Satellite("iss-zarya", True, "LEO", 42000, "20/11/1998"),
                Satellite("gps-iii-05", True, "MEO", 4331, "17/06/2021"),
                Satellite("sputnik-1", False, "LEO", 83, "04/10/1957"),
                Satellite("euclid", True, "L2", 2160, "01/07/2023")
            ]
            # self.satellite1 = Satellite("cosmo", True, "LEO", 50, "10/02/2026")
            # self.satellite2 = Satellite("sentinel-1a", True, "SSO", 2300, "03/04/2014")
            # self.satellite3 = Satellite("hubble", True, "LEO", 11110, "24/04/1990")
            # self.satellite4 = Satellite("galileo-foc1", True, "MEO", 700, "24/05/2016")
            # self.satellite5 = Satellite("meteosat-11", True, "GEO", 2000, "15/07/2015")
            # self.satellite6 = Satellite("james-webb", True, "L2", 6200, "25/12/2021")
            # self.satellite7 = Satellite("envisat", False, "SSO", 8211, "01/03/2002")
            # self.satellite8 = Satellite("starlink-3011", True, "LEO", 260, "12/05/2022")
            # self.satellite9 = Satellite("iss-zarya", True, "LEO", 42000, "20/11/1998")
            # self.satellite10 = Satellite("gps-iii-05", True, "MEO", 4331, "17/06/2021")
            # self.satellite11 = Satellite("sputnik-1", False, "LEO", 83, "04/10/1957")
            # self.satellite12 = Satellite("euclid", True, "L2", 2160, "01/07/2023")
            
    def test_aggiungi_evento(self):
    #     self.satellite1.aggiungi_evento("Evento Test") #aggiungo la lista
    #     self.assertTrue(len(self.satellite1.registroEventi.lista_eventi) > 0) #ritorna true se la lista non è 0 (prova che è stato aggiunto)
        nomeSatellite = input("Nome satellite: ")
        for satellite in self.satelliti:
            if nomeSatellite == satellite.nome:
                evento = "test evento"
                satellite.aggiungi_evento(evento)           
    
    def test_aumento_distanza(self):
        distanza = 30.2
        nomeSonda = input("Nome sonda da cercare: ")
        for sonda in self.sonde:
            if nomeSonda == sonda.nome:
                sonda.avanza(distanza)
    #     self.sonda1.avanza(30) #incrementiamo
    #     self.assertTrue(self.sonda1.distanza_percorsa > 2.55e10)
    #     self.assertFalse(self.sonda1.distanza_percorsa == 2.55e10)
    
    #testiamo le eccezzioni
    def test_aggiungi_satellite(self):
        #Scorro il primo fino al 10(quindi indice 9--> 1 indice, 9 indice)
        for satellite in self.satelliti[:10]:
            self.centroControllo.aggiungi_satellite(satellite)
            
        with self.assertRaisesRegex(CentroAlCompleto, "Massimo 10 satelliti gestiti"):
            self.centroControllo.aggiungi_satellite(self.satelliti[10]) #prendo l'11 esimo satellite in indice 10
            
        with self.assertRaises(CentroAlCompleto):
            self.centroControllo.aggiungi_satellite(self.satelliti[10]) 

    def test_aggiungi_sonda(self):
        for sonda in self.sonde[:10]:
            self.centroControllo.aggiungi_sonda(sonda)
        
        with self.assertRaises(CentroAlCompleto):
            self.centroControllo.aggiungi_sonda(self.sonde[10])
        
        with self.assertRaisesRegex(CentroAlCompleto, "Massimo 10 sonde gestite"):
            self.centroControllo.aggiungi_sonda(self.sonde[10]) 


# if __name__ == "__main__":
#     unittest.main()
    
    
'''ESECUZIONE DEL CODICE'''

def pulisci_schermo():
    # Comando per pulire la console (funziona sia su Windows che su Mac/Linux)
    os.system('cls' if os.name == 'nt' else 'clear')

def sequenza_di_avvio():
    pulisci_schermo()
    print("Inizializzazione sistema...")
    time.sleep(1)
    print("Connessione ai satelliti LEO, MEO e GEO...")
    time.sleep(1.5)
    print("Calibrazione telemetria sonde interstellari...")
    time.sleep(1)
    print("Sistemi online. Accesso garantito.\n")
    time.sleep(1)
    pulisci_schermo()

def mostra_interfaccia():
    # Avvia la finta sequenza di boot
    sequenza_di_avvio()
    controlRoom = CentroControllo()
    
    # Stampa l'interfaccia vera e propria
    print("=" * 65)
    print(r"""
     __  __    _    ____ _____ _____ ____  
    |  \/  |  / \  / ___|_   _| ____|  _ \ 
    | |\/| | / _ \ \___ \ | | |  _| | |_) |
    | |  | |/ ___ \ ___) || | | |___|  _ < 
    |_|  |_/_/   \_\____/ |_| |_____|_| \_\
                                           
      C O N T R O L   R O O M   O S  v2.0
    """)
    print("=" * 65)
    
    while True:
        # Il metodo .center() centra il testo riempiendo gli spazi vuoti con il carattere scelto
        print(" [ SYSTEM STATUS: ONLINE ] ".center(65, "-"))
        print("\n      >>> WELCOME TO THE MASTER CONTROL ROOM TERMINAL <<<\n")
        print("=" * 65)
        print("  [ 1 ] aggiungi satellite")
        print("  [ 2 ] aggiungi sonda")
        print("  [ 3 ] Report tecnico satellite")
        print("  [ 4 ] Report tecnico sonda")
        print("  [ 5 ] avanza distanza sonda")
        print("  [ 6 ] check carburante")
        print("  [ 7 ] aggiungi eventi")
        print("  [ 8 ] Disconnessione e spegnimento sistema")
        print("=" * 65)
        
        # Chiede all'utente di inserire un comando
        scelta = int(input("\nadmin@control-room:~$ Seleziona un comando [1-5]: "))
        
        print(f"\nHai selezionato il protocollo {scelta}. Esecuzione in corso...")
        
        if scelta == 1:
            try:
                id = int(input("id: "))
            except ValueError:
                print("id non valido")
            nome = input("Nome: ")
            stato = True
            orbita = input("Orbita: ")
            carburante = input("Carburante: ")
            timeStamp = input("timeStamp: ")
            
            satellite = Satellite(nome, stato, orbita, carburante, timeStamp)
            controlRoom.aggiungi_satellite(id, satellite)
            
        elif scelta == 2:
            nome = input("Nome: ")
            stato = True
            destinazione = input("Destinazione: ")
            distanza_percorsa = input("distanza percorsa: ")
            
            sonda = Sonda(nome, stato, destinazione, distanza_percorsa)
            controlRoom.aggiungi_sonda(sonda)
            
        elif scelta == 3:
            operatore = input("operatore: ")
            controlRoom.report_tecnico_satellite(operatore)
            
        elif scelta == 4:
            operatore = input("> ")
            controlRoom.report_tecnico_sonda(operatore)
            
    
if __name__ == "__main__":
    mostra_interfaccia()