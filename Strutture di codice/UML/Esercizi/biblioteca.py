'''Traccia: Sistema Biblioteca
Contesto: Progetta un sistema per gestire una biblioteca con libri, lettori e bibliotecari.
Entità del sistema:
Una Persona come classe base. Un Lettore che prende libri in prestito. Un Bibliotecario che gestisce i prestiti. Un Libro con una sua scheda descrittiva. Una Biblioteca che coordina tutto.
Relazioni richieste:

Almeno una ereditarietà
Almeno una composizione
Almeno una aggregazione
Almeno una associazione

Vincoli semantici con @property:

L'età deve essere tra 6 e 99
Un lettore può avere massimo 3 libri in prestito contemporaneamente

Eccezioni da gestire:

Libro non disponibile
Libro non trovato
Età non valida (try-except)
Lettore ha già troppi libri in prestito

Il sistema deve permettere di:

Aggiungere libri e lettori alla biblioteca
Registrare un prestito
Cercare un libro per titolo
Stampare il report completo'''
#Eccezioni customizzate
class Libro_non_disponibile(Exception):
    pass
class Libro_non_trovato(Libro_non_disponibile):
    pass
class troppi_libri(Libro_non_disponibile):
    pass

class Persona():
    def __init__(self, nome, cognome, eta):
        self.__nome = nome
        self.__cognome = cognome
        self.__eta = eta
        
    #Incapsulamento
    @property
    def nome(self):
        return self.__nome
    @property
    def cognome(self):
        return self.__cognome
    @property
    def eta(self):
        return self.__eta
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
        
    @cognome.setter
    def cognome(self, cognome):
        self.__cognome = cognome
        
    @eta.setter
    def eta(self, eta):
        if eta < 6 or eta > 99:
            raise ValueError("Età non valida")
        self.__eta = eta
        
    def __str__(self):
        return f"Persona -> | nome: {self.nome} | cognome: {self.cognome} | eta: {self.eta}"
    
class Libro():
    def __init__(self, titolo, autore, costo):
        self.titolo = titolo
        self.autore = autore
        self.costo = costo
        
    def __str__(self):
        return f"Scheda Libro: | titolo: {self.titolo} | autore: {self.autore} | costo: {self.costo}"

#Extends Persona           
class Lettore(Persona):
    def __init__(self, nome, cognome, eta):
        super().__init__(nome, cognome, eta)
        
        self.lista_personale_libri = []
        
    #Metodo per prendere un libro
    def prenota_libro(self, libro): #associazione di libro
        if len(self.lista_personale_libri) > 3:
            raise troppi_libri("il lettore ha già troppi libri")
        else:
            self.lista_personale_libri.append(libro) #aggrego Libro() alla lista di Lettore
            print("[LOG] libro prenotato")
            
        for libro in self.lista_personale_libri:
            print(libro)
            
        # for x in range(0,3):
        #     self.lista_personale_libri.append(libro)
        #     print(f"[LOG] libro aggiunto alla lista {x+1}")
    def __str__(self):
        return f" Scheda Lettore -> | nome: {self.nome} | cognome: {self.cognome} | eta: {self.eta}"

#Extends Persona
class Bibliotecaria(Persona):
    def __init__(self, nome, cognome, eta):
        super().__init__(nome, cognome, eta)
        
        self.libri_disponibili = []
        self.database_prestiti = {}
        
    def gestore_libri_prenotati(self, lettore, libro):
        self.database_prestiti[str(lettore)] = str(libro) #Aggregazione
        
        # for x in self.database_prestiti.items():
        #     print(x)
            
    def aggiungi_libri(self, libro):
        libro =  {
            "titolo":libro.titolo,
            "autore":libro.autore,
            "costo":libro.costo
        }
        
        self.libri_disponibili.append(libro)
        
        # for x in self.libri_disponibili:
        #     print(x)
    
    def cercaLibro (self):
        for x in self.libri_disponibili:
            print(x)
    
    def __str__(self):
        return f"Operatore Bicliotecario/a -> | nome: {self.nome} | cognome: {self.cognome} | eta: {self.eta}"
        
        

class Biblioteca():
    def sistema_centralizato():
        lettore = Lettore("Davide","Gatta", 23)   
        while True:
            print("\n")
            print("╔════════════════════════════╗")
            print("║    TERMINALE BIBLIOTECA    ║")
            print("╚════════════════════════════╝")
            
            
            print("\n[ MENU ]")
            print("1 ➜ Prenota libro")
            print("2 ➜ Gestore libri prenotati")
            
            scelta = int(input("> "))
            
            if scelta == 1:
                #piccolo controllo se il libro esiste ed è disponibile
                print("check della disponibilià per titolo")
                titolo = input("titolo: ")
                
                if titolo in bibliotecaria.libri_disponibili["titolo"]:
                    print("[LOG] libro trovato")
                
                print("Inserisci le infomazioni mancanti: ")
                autore = input("autore: ")
                costo = float(input("costo: "))
                libro = Libro(titolo, autore, costo)
                
                lettore.prenota_libro(libro)
                
                '''TODO Davide. Finire la classe centralizzata perla gestione di tutti gli attributi e metodi'''
                
                    
                    
                    

                
                
        
    
#Regione di test
libro = Libro("Divina commedia","Dante", 10.5)
libro1 = Libro("Promessi sposi", "Manzoni", 15.4)

lettore = Lettore("Davide","Gatta", 23)
bibliotecaria = Bibliotecaria("Mario","Rossi", 35)

lettore.prenota_libro(libro)
lettore.prenota_libro(libro1)

bibliotecaria.gestore_libri_prenotati(lettore, libro)
bibliotecaria.gestore_libri_prenotati(lettore, libro1)

bibliotecaria.aggiungi_libri(libro)