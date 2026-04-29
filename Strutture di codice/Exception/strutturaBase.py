'''Il blocco try contiene il codice "rischioso". Se si verifica un errore, Python salta subito al blocco except.'''

try: #Codice rischioso
    numero = int(input("Inserisci numero: "))
    risultato = 10 / numero
    print(f"Risultato: {risultato}")

except ValueError: #Se inserisco una lettara nella variabile numero
    print("Hai inserito un valore non numerico")

except ZeroDivisionError: #Se inserisco uno 0
    print("Non puoi dividere per zero")