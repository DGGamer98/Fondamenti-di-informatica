def addizioni(a,b):
    somma = a + b
    return somma
    
def sottrazioni(a,b):
    sottrazioni = a - b
    return sottrazioni
    
def moltiplicazioni(a,b):
    risultato = a * b
    return risultato
    
def divisione(a,b):
    try:
        divisone = a / b
        return divisone
    except ZeroDivisionError:
        return "Attenzione divisone per 0"

a = int(input("numero1 "))
b = int(input("numero2 "))

addizioneRisult = addizioni(a,b)
sottrazioneRisult = sottrazioni(a,b)
moltiplicazioniRisult = moltiplicazioni(a,b)
divisioneRisult = divisione(a,b)

print("somma = ",addizioneRisult)
print("Sottrazioni = ", sottrazioneRisult)
print("Moltiplicazioni = ", moltiplicazioniRisult)
print("divisione = ", divisioneRisult)