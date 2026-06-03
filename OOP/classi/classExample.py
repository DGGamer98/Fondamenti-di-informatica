#Struttura --> astrazione di un oggetto
class Satellite:
    def __init__(self, nome, orbita): #costruttores
        #attributi di istanza
        self.nome = nome
        self.orbita = orbita
        self.carburante = 100 # valori default
        
    def consuma(self, quantità):
        self.carburante-=quantità
        print(self.carburante)
        
        

#creazione di 2 oggetti
s1 = Satellite("Cosmo","GEO")
s1.consuma(30)
s2 = Satellite("Prisma","LEO")
print(s2.carburante)



#accesso agli attributi
print(s1.nome)
print(s2.orbita)

'''SELF --> riferimento all'oggetto stesso'''        
    