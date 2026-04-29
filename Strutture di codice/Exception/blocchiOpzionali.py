try:
    numero = int(input("Numero: "))
    #invece di fare il print uso l'else
except ValueError:
    print("Errore: non è un numero! ")
else:
    print(f"Ottimo! hai inserito {numero}") # solo se ok 

finally:
    print("Fine operazione") #Eseguito sempre