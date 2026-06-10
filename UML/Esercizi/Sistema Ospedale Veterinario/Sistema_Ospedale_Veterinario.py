import unittest


#Exception customizzate
class Clinica_al_completo(Exception):
    pass
class Animale_non_trovato(Exception):
    pass
class Peso_non_valido(Exception):
    pass
class Massimo_4_animali(Exception):
    pass
class eta_non_valida(Exception):
    pass

class Persona():
    def __init__(self, nome, cognome, eta):
        self.__nome = nome
        self.__cognome = cognome
        self.eta = eta

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
        if eta >= 18:
            self.__eta = eta
            print("[LOG] maggiorenne")
            return True
        else:
            raise eta_non_valida("minorenne")

    #converte in stringa l'oggetto che passiamo per associazione/aggregazione o composizione
    def __str__(self):
        return f"Persona --> | Nome: {self.nome} | Cognome: {self.cognome} | eta: {self.eta}"

#Classe figlia di Personax
class Proprietario(Persona):
    def __init__(self, nome, cognome, eta):
        super().__init__(nome, cognome, eta)
        self.animali_domestici = []

    def aggiungi_animali(self, animale, nome):
        if len(self.animali_domestici) >=4:
            raise Massimo_4_animali("Massimo 4 animali sono consentiti")

        animali = {nome:animale} #creo un dizionario e lo aggiungo alla lista
        self.animali_domestici.append(animali)
        print("[LOG] animale aggiunto")

    def portaAnimale(self, animale, veterinario): #Associazione con l'istanza della classe Animale
        return f"Il proprietario {self.nome} porta {animale} dal dott. {veterinario}"

    def __str__(self):
        return f"Proprietario --> | Nome: {self.nome} | Cognome: {self.cognome} | eta: {self.eta}"

#Classe figlia di Persona
class Veterinario(Persona):
    def __init__(self, nome, cognome, eta):
        super().__init__(nome, cognome, eta)
        self.database_visite = {}

    def visita_animale(self, animale, proprietario):
        print(f"[LOG] il veterinario {self.nome} visita: {animale}")
        self.database_visite[proprietario]=animale
        print("[LOG] visita registrata ")
        return True

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


class test_unit(unittest.TestCase):
    def setUp(self):
        self.proprietario = Proprietario("Davide","Gatta", 23)
        self.veterinario = Veterinario("Simona","Rossi", 45)
        self.animale = Animale("Nora","Felino",12, "gatto tigrato")

    def test_eta_valida(self):
        # Verifica semplicemente che l'età sia quella corretta
        self.assertEqual(self.proprietario.eta, 23)

    def test_eta_non_valida(self):
        with self.assertRaises(eta_non_valida):
            Proprietario("giovanni", "Gatta", 13)
    
    def test_visita_ok(self):
        self.assertTrue(self.veterinario.visita_animale(self.animale, self.proprietario))
    
    def test_troppi_animali(self):
        self.proprietario.aggiungi_animali(self.animale, "nora1")
        self.proprietario.aggiungi_animali(self.animale, "nora2")
        self.proprietario.aggiungi_animali(self.animale, "nora3")
        self.proprietario.aggiungi_animali(self.animale, "nora4")

        with self.assertRaisesRegex(Massimo_4_animali, "troppi animali"):
            self.proprietario.aggiungi_animali(self.animale, "tor")

if __name__ == "__main__":
    unittest.main()