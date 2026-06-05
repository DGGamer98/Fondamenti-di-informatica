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
        if len(self.lista_personale_libri) >= 3:
            raise troppi_libri("il lettore ha già troppi libri")
        else:
            self.lista_personale_libri.append(libro) #aggrego Libro() alla lista di Lettore
            print(f"[LOG] libro prenotato {libro}")
            
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
        
        #stampo tutto il contenuto del dizionario
        for x in self.database_prestiti.items():
            print(x)
            
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
            
    def rimuovi_libro(self, libro):
        self.libri_disponibili.remove(libro)
            
    
    def __str__(self):
        return f"Operatore Bicliotecario/a -> | nome: {self.nome} | cognome: {self.cognome} | eta: {self.eta}"
        
        

class Biblioteca():
    def __init__(self, nome_biblioteca, indirizzo):
        self.nome_biblioteca = nome_biblioteca
        self.indirizzo = indirizzo
        self.bibliotecaria = Bibliotecaria("Mario","Rossi", 35) #Compisizione
        self.lettore = Lettore("Davide","Gatta", 23)
        
        #Test
        #self.libro = Libro("Divina commedia","Dante", 10.5)

    def sistema_centralizato(self):
        print("Aggiungi almeno 4 libri alla biblioteca")

        for x in range(1, 4):
            titolo = input("nome: ")
            autore = input("cognome: ")
            costo = float(input("costo: "))

            libro = Libro(titolo, autore, costo)

            #aggiungo dei libri per testare il codice
            self.bibliotecaria.aggiungi_libri(libro)
            print(f"{x} libro aggiuto")
        
        self.bibliotecaria.cercaLibro()
        print("x")

        while True:
            print("\n")
            print("╔════════════════════════════╗")
            print("║    TERMINALE BIBLIOTECA    ║")
            print("╚════════════════════════════╝")
                    
            print("\n[ MENU ]")
            print("1 ➜ Prenota libro")
            print("2 ➜ Gestore libri prenotati")
            print("3 ➜ esci")

            scelta = int(input("> "))
            if scelta == 1:
                #piccolo controllo se il libro esiste ed è disponibile
                print("check della disponibilià per titolo")
                titolo = input("titolo: ")
                
                # 1. prima cerca il libro
                libro_trovato = None
                for libri in self.bibliotecaria.libri_disponibili:
                    if libri["titolo"].lower() == titolo.lower():
                        libro_trovato = libri
                        break         
                # 2. poi gestisci fuori dal loop
                try:
                    if libro_trovato is None:
                        raise Libro_non_trovato("Libro non trovato!")
                    
                    self.lettore.prenota_libro(libro_trovato)
                    self.bibliotecaria.rimuovi_libro(libro_trovato)  # ← ora rimuovi fuori dal loop
                    print("[LOG] Libro aggiunto")

                except Libro_non_trovato as e:
                    print(f"Errore: {e}")
                except troppi_libri as e:
                    print(f"Errore: {e}")
                
            elif scelta == 2:
                for l in self.lettore.lista_personale_libri:
                    print(l)
            elif scelta == 3:
                break
                
biblioteca = Biblioteca("Nardi","Roma")
biblioteca.sistema_centralizato()

