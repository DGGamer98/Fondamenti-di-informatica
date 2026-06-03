# eccezione base da cui ereditano le altre
class ParcheggioException(Exception):
    pass

class PostoOccupato(ParcheggioException):
    pass

class PostoNonEsistente(ParcheggioException):
    pass

class PostoGiaLibero(ParcheggioException):
    pass

class TargaInvalida(ParcheggioException):
    pass

class Parcheggio:
    def __init__(self, posti_totale):
        self.posti = [None] * posti_totale

    def parcheggia(self, numero_posto, targa):
        if self.posti[numero_posto] is not None:
            raise PostoOccupato("Il posto è già occupato!")
        
        if numero_posto >= len(self.posti):
            raise PostoNonEsistente("Il parcheggio indicato non esiste")
        else:
            self.posti[numero_posto] = targa
            print("[LOG] posto assegnato")
            return
        
    def libera(self, numero_posto):
        if numero_posto >= len(self.posti):
            raise PostoNonEsistente("Il posto non esiste!")
        
        if self.posti[numero_posto] is None:
            raise PostoGiaLibero("Il posto è già libero!")
        
        self.posti[numero_posto] = None 
        print("[LOG] posto liberato")

    def cerca_auto(self, targa):
        if targa not in self.posti:
            raise ValueError ("Targa non trovata")
        
        for auto in self.posti:
            if targa == auto:
                return self.posti.index(targa)

    def stampa(self):
        for x in self.posti:
            print(x)
        
p = Parcheggio(3)
p.parcheggia(2,"BA23CZX")
p.stampa()

print(p.cerca_auto("ZZZZ"))

# p.libera(34)
# p.stampa()



