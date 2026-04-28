class Astronauta:
    agenzia = "ESA"
    
    def __init__(self,nome,nazionalità):
        self.nome = nome
        self.nazionalità = nazionalità
        self.missioni =  []
        self.ore_volo = 0
        
    def aggiungi_missione(self, nome_missione):
        self.missioni.append(nome_missione)
        print("[LOG] Missione aggiunta")
        return
        
    def vola(self, ore):
        self.ore_volo += ore 
        return self.ore_volo
    
    def is_esperto(self):
        if self.ore_volo > 500:
            return True
        else:
            return False
        
    def __str__(self):
        return f"{self.nome}, {self.nazionalità}, {self.missioni}, {self.ore_volo}"
    
    
    
s1 = Astronauta("Luca parmitano","Italiana")
s2 = Astronauta("Paolo Nespoli","Italiana")

s1.aggiungi_missione("artemis III")
s2.aggiungi_missione("Artemis II")

print(f"Luca parmitano ore volo {s1.vola(30)} con {s1.agenzia}")
print(f"Paolo Nespoli ore volo {s2.ore_volo} con {s1.agenzia}")




    
        
        
        