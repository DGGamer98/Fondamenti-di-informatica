def numeroMAX(numero1, numero2):
    if numero1 > numero2:
        print(f"il numero {numero1} è più grande di {numero2}")
    elif numero2 > numero1:
        print(f"il numero {numero2} è più grande di {numero1}")
    else:
        print("i numeri sono uguali ")
    
    
numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))

numeroMAX(numero1, numero2)