'''Mostra la differenza tra variabili globali e locali'''
def print_successivo(n):
    var = 3 #var e n sono visibili solo dentro la funzione
    n+=1
    print("n locale", n)
    
if __name__ == "__main__":
    n = 10
    print("n globale prima", n)
    print_successivo(n)
    print("n globale dopo", n)