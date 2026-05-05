# crea queste eccezioni
class DistributoreException(Exception):
    pass

class ProdottoEsaurito(DistributoreException):
    pass

class SoldiInsufficienti(DistributoreException):
    pass

class ProdottoNonEsistente(DistributoreException):
    pass


class Distributore:
    def __init__(self):
        self.prodotti = {
            "acqua":{ "prezzo":1.0, "quantita": 3 },
            "caffè":{ "prezzo":1.5, "quantita": 2 },
            "succo":{ "prezzo":2.0, "quantita": 0}
        }

    def acquista(self, nome_prodotto, soldi_inseriti):
    
        if nome_prodotto not in self.prodotti:
            raise ProdottoNonEsistente(f"{nome_prodotto} non esiste!")
        
        prodotto = self.prodotti[nome_prodotto]  # ← prendi il dizionario del prodotto
        
        if prodotto["quantita"] == 0:
            raise ProdottoEsaurito(f"{nome_prodotto} esaurito!")
        
        if soldi_inseriti < prodotto["prezzo"]:
            raise SoldiInsufficienti(f"Servono {prodotto['prezzo']}€, inseriti {soldi_inseriti}€")
        
        prodotto["quantita"] -= 1                    # ← -= non solo -
        resto = soldi_inseriti - prodotto["prezzo"]  # ← resto non prezzo!
        print(f"Hai acquistato {nome_prodotto}! Resto: {resto}€")
            

d = Distributore()
try:
    d.acquista("acqua", 2.0)   
except DistributoreException as e:
    print(f"Errore: {e}")

try:
    d.acquista("birra", 2.0)    
except DistributoreException as e:
    print(f"Errore: {e}")

try:
    d.acquista("succo", 5.0)    
except DistributoreException as e:
    print(f"Errore: {e}")

try:
    d.acquista("caffè", 0.5)    
except DistributoreException as e:
    print(f"Errore: {e}")