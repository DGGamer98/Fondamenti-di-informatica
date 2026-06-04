import unittest

#Eccezioni customizzate
class Gioco_non_disponibile(Exception):
    pass
class Gioco_non_trovato(Gioco_non_disponibile):
    pass
class Negozio_al_completo(Exception):
    pass
class Troppi_noleggi_attivi(Exception):
    pass

class Persona():
    def __init__(self, nome, cognome, eta):
        self.__nome = nome
        self.__cognome = cognome
        self.eta = eta
    
    #Getter dato in sola lettura    
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
            
        self.__eta = eta
    def __str__(self):
        return f"Nome: {self.__nome} Cognome: {self.__cognome} eta: {self.__eta}"
    
class Cliente(Persona):
    def __init__(self, nome, cognome, eta):
        super().__init__(nome, cognome, eta)
        #Racchiudo gli oggetti nelle liste --> aggregazione
        self.lista_noleggi_personale = []
        self.lista_aquisti_personale = []
        
    #associazione di videogioco
    def Aquista(self, video_gioco):
        self.lista_aquisti_personale.append(video_gioco)
        print("[LOG] gioco acquistato")
    
    def Noleggia(self, video_gioco):
        if len(self.lista_noleggi_personale) >= 3:
            raise Troppi_noleggi_attivi("Hai superato i 3 noleggi consentiti")

        self.lista_noleggi_personale.append(video_gioco)
        print("[LOG] gioco noleggiato")

class Commesso(Persona):
    def __init__(self, nome, cognome, eta):
        super().__init__(nome, cognome, eta)
        self.vendite_effettuate = {}
        
    #Associa Cliente e viedogioco
    def gestioneVendite(self, Cliente, video_gioco):
        self.vendite_effettuate[Cliente] = video_gioco
        print("[LOG] vendita effetuata")
    
    #associo negozio per controllare se il gioco è disponibile
    def gioco_disponibile(self, titolo, negozio):
        #Scorro la lista della classe negozio --> altrimenti si ferma alla prima iterazione e lancia eccezione
        for elemento in negozio:
            if titolo in elemento:
                print("[LOG] Gioco trovato")
                return True
        raise Gioco_non_trovato("[Error] Il gioco non è disponibile nel negozio")
    
class VideoGioco():
    def __init__(self, titolo, costo, peghi, genere):
        self.__titolo = titolo
        self.costo = costo
        self.__peghi = peghi
        self.__genere = genere
        
    @property
    def titolo(self):
        return self.__titolo
    @property
    def costo(self):
        return self.__costo
    @property
    def peghi(self):
        return self.__peghi
    @property
    def genere(self):
        return self.__genere
    
    @costo.setter
    def costo(self, costo):
        if costo > 0:
            print("[LOG] ok")
            self.__costo = costo
        elif costo <= 0:
            raise ValueError ("[Error] il gioco non può costare 0")
 
    def __str__(self):
        return f"Scheda Tecnica: | Titolo: {self.titolo} | costo: {self.costo} | peghi: {self.peghi} | genere: {self.genere}"

class Negozio():
    def __init__(self, nome_negozio, indirizzo):
        self.nome_negozio = nome_negozio
        self.indirizzo = indirizzo
        self.magazino_giochi = []
    
    #uso l'associazione per aggiungere video gioco al magazino    
    def aggiungi_giochi_magazino(self, titolo, video_gioco):
        gioco = {titolo: video_gioco}
        self.magazino_giochi.append(gioco)
        print("[LOG] gioco aggiunto con successo")

    def rimuovi_gioco(self, titolo):
        for elemento in self.magazino_giochi:
            if titolo in elemento:
                self.magazino_giochi.remove(elemento) #elemento equivale a un'intero dizionario
                print("[LOG] gioco rimosso")
                return True
        

if __name__ == "__main__":
            # Dati cliente
        cliente1 = Cliente("Davide", "Gatta", 23)
        cliente2 = Cliente("Ciro", "Rossi", 10)

        # Dati Commesso
        commesso1 = Commesso("Alfredo", "Bianchi", 33)

        game_stop = Negozio("gameStop","Roma est")
        
        # Dati gioco
        gioco1 = VideoGioco("The Legend of Zelda: Tears of the Kingdom", 69.99, 12, "Avventura")
        gioco2 = VideoGioco("Elden Ring", 59.99, 16, "Action RPG")
        gioco3 = VideoGioco("Super Mario Odyssey", 49.99, 3, "Platform")
        gioco4 = VideoGioco("Cyberpunk 2077", 39.99, 18, "Fantascienza / RPG")

        game_stop.aggiungi_giochi_magazino("The Legend of Zelda", gioco1)
        game_stop.aggiungi_giochi_magazino("Elden Ring", gioco2)
        game_stop.aggiungi_giochi_magazino("Super Mario Odyssey", gioco3)
        game_stop.aggiungi_giochi_magazino("Cyberpunk 2077", gioco4)

        # if commesso1.gioco_disponibile("Elden Ring", game_stop.magazino_giochi):
        #     cliente1.Aquista(gioco1)
        #     game_stop.rimuovi_gioco("Elden Ring")

        cliente1.Noleggia(gioco1)
        cliente1.Noleggia(gioco2)
        cliente1.Noleggia(gioco3)
        cliente1.Noleggia(gioco4)



# class test_store(unittest.TestCase):
#     def setUp(self):
#         # NOTA: Usiamo "self." per rendere le variabili accessibili negli altri metodi
#         # Dati cliente
#         self.cliente1 = Cliente("Davide", "Gatta", 23)
#         self.cliente2 = Cliente("Ciro", "Rossi", 10)
        
#         # Dati Commesso
#         self.commesso1 = Commesso("Alfredo", "Bianchi", 33)
        
#         # Dati videogiochi
#         self.gioco1 = VideoGioco("The Legend of Zelda: Tears of the Kingdom", 69.99, 12, "Avventura")
#         self.gioco2 = VideoGioco("Elden Ring", 59.99, 16, "Action RPG")
#         self.gioco3 = VideoGioco("Super Mario Odyssey", 49.99, 3, "Platform")
#         self.gioco4 = VideoGioco("Cyberpunk 2077", 39.99, 18, "Fantascienza / RPG")
        

#     def test_eta_valida(self):
#         self.assertEqual(self.cliente2.eta, 10)
        
#     def test_eta_troppo_piccola_lancia_eccezione(self):
#         # Verifica che il setter lanci un ValueError se proviamo a inserire un'età inferiore a 10
#         with self.assertRaises(ValueError):
#             Cliente("Bambino", "Piccolo", 9)
    

            
