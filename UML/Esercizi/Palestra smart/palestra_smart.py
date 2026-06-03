import unittest

class Persona():
    def __init__(self,nome,cognome,eta):
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
    def nome(self, nome):
        self.__nome = nome
    @cognome.setter
    def cognome(self, cognome):
        self.__cognome = cognome
    @eta.setter
    def eta(self, eta):
        if eta >= 16 and eta <= 80:
            print("[LOG] eta ok")
        else:
            raise ValueError ("[Error] eta non valida")
            
    def __str__(self):
        return (
            f"nome: {self.nome}\n"
            f"Cognome: {self.cognome}\n"
            f"Età: {self.eta}"
        )

class Attrezzatura():
    def __init__(self, nome_attrezzo, scheda_tecnica):
        self.nome_attrezzo = nome_attrezzo
        self.scheda_tecnica = scheda_tecnica
        self.descrizione = {}
    
    def descrizione_attrezzo(self):
        self.descrizione[self.nome_attrezzo] = [self.scheda_tecnica]
        print("[LOG] attrezzo aggiunto all'attrezzatura")
        
        # for x in self.descrizione.items():
        #     print(x)
        
    #il metodo serve se un attrezzo viene preso un prestito
    def rimuovi_attrezzo(self):
        self.descrizione.pop(self.nome_attrezzo)
        
    def __str__(self):
        unionString = ", ".join(str(v) for v in self.descrizione.items())
        return f"Scheda tecnica: {unionString}"
        
         
#Eredito persona
class Membro(Persona):
    def __init__(self, nome, cognome, eta):
        super().__init__(nome, cognome, eta)
        self.attrezzature_in_prestito = []
    
    def usa_attrezzature(self, attrezzatura): #associazione attrezzatura
        self.attrezzature_in_prestito.append(attrezzatura)
        
        # for x in self.attrezzature_in_prestito:
        #     print(x)
        
    def __str__(self):
        attrezzatura_presa = ", ".join(str(v) for v in self.attrezzature_in_prestito)
        return f"Il Membro {self.nome} {self.cognome} di eta {self.eta} a i seguenti attrezzi {attrezzatura_presa}"
    
class Istruttore(Persona):
    def __init__(self, nome, cognome, eta):
        super().__init__(nome, cognome, eta)
        
        self.sessioni_in_corso = {}
        
    def gestione_sessioni(self, membro, attrezzo):
        self.sessioni_in_corso[str(membro)] = str(attrezzo)
    
    def __str__(self):
        return (
            f"Istruttore: {self.nome}\n"
            f"Cognome: {self.cognome}\n"
            f"Età: {self.eta}\n"
            f"Segue: {self.sessioni_in_corso}\n"
            )

    
'''Parte di codice per test'''

membro = Membro("Davide", "Gatta", 23)

membro1 = Membro("Alfonso", "verde", 11)
#membro1.eta = 12

parallele = Attrezzatura("parallele","usate per allenare il petto e braccia")
pesi = Attrezzatura("pesi","usati per allenare le braccia")
istruttore = Istruttore("Luca","Rossi",35)

parallele.descrizione_attrezzo()
pesi.descrizione_attrezzo()
# parallele.rimuovi_attrezzo()
# pesi.rimuovi_attrezzo()

membro.usa_attrezzature(parallele)
membro.usa_attrezzature(pesi)

membro1.usa_attrezzature(pesi)

istruttore.gestione_sessioni(membro, pesi)
istruttore.gestione_sessioni(membro1, pesi)

# alla fine del codice aggiungi:

print(f"{istruttore} \n")


'''Parte di unittest'''
class Test_Palestra(unittest.TestCase):
    def setUp(self):
        membro = Membro("Davide", "Gatta", 23)
        membro1 = Membro("Alfonso", "verde", 16)
        parallele = Attrezzatura("parallele","usate per allenare il petto e braccia")
        pesi = Attrezzatura("pesi","usati per allenare le braccia")
        istruttore = Istruttore("Luca","Rossi",35)  

    def test_eta_valida(self):
        persona = membro
        self.assertEqual(membro, persona)

    def test_eta_non_valida(self):
        with self.assertRaises(ValueError):
            membro1.eta = 12

    def test_attrezzatura_non_disponibile(self):
        with self.assertRaises(ValueError):
            parallele.rimuovi_attrezzo()
            pesi.rimuovi_attrezzo()

if __name__ == "__main__":
    unittest.main() 