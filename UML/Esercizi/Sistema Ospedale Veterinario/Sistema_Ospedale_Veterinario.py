'''
1️⃣ Traccia: Sistema Ospedale Veterinario
Contesto: Gestisci una clinica veterinaria con animali, proprietari e veterinari.
Entità del sistema:
Una Persona come classe base. Un Proprietario che porta gli animali. Un Veterinario che visita gli animali. Un Animale con una sua cartella clinica. Una Clinica che coordina tutto.
Relazioni richieste:

Almeno una ereditarietà
Almeno una composizione
Almeno una aggregazione
Almeno una associazione

Vincoli semantici con @property:

L'età del proprietario deve essere tra 18 e 90
Il peso dell'animale deve essere maggiore di 0
Un proprietario può avere massimo 4 animali registrati

Eccezioni da gestire:

Animale non trovato
Troppi animali registrati
Età non valida
Peso non valido
Clinica al completo

Test con unittest:

test_eta_valida — assertEqual
test_eta_non_valida — assertRaises
test_visita_ok — assertTrue
test_troppi_animali — assertRaisesRegex
test_peso_non_valido — assertRaises
'''
#Exception customizzate
class Clinica_al_completo(Exception):
    pass
class Animale_non_trovato(Exception):
    pass
class Peso_non_valido(Exception):
    pass

class Persona():
    def __init__(self, nome, cognome, eta):
        self.__nome = nome
        self.__cognome = cognome
        self.__eta = eta

    #Incapsulamento
    #accesso in sola lettura
    @property
    def nome(self):
        return self.__nome
    @property
    def cognome(self):
        return self.__cognome
    @property
    def eta(self):
        return self.__eta
    
    #Setter
    @eta.setter
    def eta(self, eta):
        try:
            if eta > 18:
                self.__eta = eta
                print("[LOG] maggiorenne")
                return True
        except ValueError as e:
            print(f"minorenne, {e}")

    #converte in stringa l'oggetto che passiamo per associazione/aggregazione o composizione
    def __str__(self):
        return f"Persona --> | Nome: {self.nome} | Cognome: {self.cognome} | eta: {self.eta}"

#Classe figlia di Persona
class Proprietario(Persona):
    def __init__(self, nome, cognome, eta):
        super().__init__(nome, cognome, eta)

    def portaAnimale(self, animale, veterinario): #Associazione con l'istanza della classe Animale
        pass

    def __str__(self):
        return f"Proprietario --> | Nome: {self.nome} | Cognome: {self.cognome} | eta: {self.eta}"

#Classe figlia di Persona
class Veterinario(Persona):
    def __init__(self, nome, cognome, eta):
        super().__init__(nome, cognome, eta)

    def visita_animale(self, animale, proprietario):
        pass

    def __str__(self):
        return f"Veterinario --> | Nome: {self.nome} | Cognome: {self.cognome} | eta: {self.eta}"
    
#Classe a se
class Animale():
    def __init__(self, nome_animale, tipo_animale, eta, razza):
        self.__nome_animale = nome_animale
        self.__tipo_animale = tipo_animale
        self.__eta = eta
        self.__razza = razza

    #Accesso in sola lettura
    @property
    def nome_animale(self):
        return self.__nome_animale
    @property
    def tipo_animale(self):
        return self.__tipo_animale
    @property
    def eta(self):
        return self.__eta
    @property
    def razza(self):
        return self.__razza
    
    #setter
    #accesso ai metodi per inizializare nuovi valori agli attributi di istanza
    #Lettura e scrittura
    @nome_animale.setter
    def nome_animale(self, nome_animale):
        self.__nome_animale = nome_animale
    @tipo_animale.setter
    def tipo_animale(self, tipo_animale):
        self.__tipo_animale = tipo_animale
    @eta.setter
    def eta(self, eta):
        self.__eta = eta
    @razza.setter
    def razza(self, razza):
        self.__razza = razza

    def __str__(self):
        return f"Animale --> | nome animale: {self.nome_animale} | tipo animale: {self.tipo_animale} | eta: {self.eta} | razza: {self.razza}"


class Clinica_Veterinaria():
    def main(self):            
        proprietario = Proprietario("Davide","Gatta", 23)
        veterinario = Veterinario("Simona","Rossi", 45)
        animale = Animale("Nora","Felino",12, "gatto tigrato")

        print(proprietario)
        print(veterinario)
        print(animale)


clinica = Clinica_Veterinaria()
clinica.main()