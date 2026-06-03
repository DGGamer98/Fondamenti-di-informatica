'''Puoi lanciare eccezioni manualmente con raise, e creare eccezioni personalizzate ereditando da Exception.'''

#Lancio di un'eccezzione manualmente
def dividi(a, b):
    if b == 0:
        raise ValueError ("il divisore non può essere zero")
    return a / b


#Eccezione customizzata
class CarburanteInsufficienti(Exception):
    pass

def lancia_razzo(carburante):
    if carburante < 20:
        raise CarburanteInsufficienti("Carburante troppo basso")
    print("Lancio avvenuto")

try:
    lancia_razzo(10)
except CarburanteInsufficienti as e:
    print(f"[ALERT] {e}")

print(dividi(10,4))

