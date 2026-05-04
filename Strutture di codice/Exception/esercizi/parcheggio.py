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

'''TODO Davide
class Parcheggio:
    def __init__(self, posti_totali):
        # crea una lista di posti: [None, None, None, ...]
        # None = libero, stringa = targa dell'auto

    def parcheggia(self, numero_posto, targa):
        # raise PostoNonEsistente se numero_posto fuori range
        # raise TargaInvalida se targa è vuota o ha meno di 4 caratteri
        # raise PostoOccupato se il posto non è None
        # altrimenti parcheggia l'auto

    def libera(self, numero_posto):
        # raise PostoNonEsistente se numero_posto fuori range
        # raise PostoGiaLibero se il posto è già None
        # altrimenti libera il posto

    def cerca_auto(self, targa):
        # cerca la targa in tutti i posti
        # raise ValueError se non trovata
        # restituisce il numero del posto

    def mostra_parcheggio(self):
        # stampa tutti i posti con stato libero/occupato
'''

        

