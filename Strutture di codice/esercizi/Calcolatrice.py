while True:
    print("1 Addizzione")
    print("2 Sottrazione")
    print("3 Moltiplicazione")
    print("4 Divisione")
    print("5 esci")
    
    scelta = int(input("> "))
    
    if scelta == 1:
        a = int(input("Numero1: "))
        b = int(input("Numero2: "))
        
        somma = a + b
        print(somma)
    elif scelta == 2:
        a = int(input("Numero1: "))
        b = int(input("Numero2: "))
        
        sottrazione = a - b
        print(sottrazione)
    elif scelta == 3:
        a = int(input("Numero1: "))
        b = int(input("Numero2: "))
        
        moltiplicazione = a*b
        print(moltiplicazione)
    elif scelta == 4:
        a = int(input("Numero1: "))
        b = int(input("Numero2: "))
        
        try:
            divisone = a / b
            print(divisone)
        except ZeroDivisionError:
            print("Attenzione divisone per 0")
    elif scelta == 5:
        break