class Rettangolo:
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    # def Area(self):
    #     self.area = self.base*self.altezza
    #     return self.area
     
    #     self.perimetro = 2*(self.base + self.altezza)
    #     return self.perimetro
    def Area(self):
        return self.base * self.altezza
    
    def Perimetro(self):
        return 2*(self.base + self.altezza)

    def descrizione(self):
        print(f"Rettangolo di base: {self.base} e altezza: {self.altezza}")

        print(f"Area: {self.Area()}")
        print(f"Perimetro: {self.Perimetro()}")

        #print(f"Area:{self.area}")
        #print(f"Perimetro: { self.perimetro}")

r1 = Rettangolo(5,8)

r1.Area()
r1.Perimetro()

r1.descrizione()
