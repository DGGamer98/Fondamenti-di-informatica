def trovaIlMassimo(a,b,c):
    if a > b and a > c:
        print(f"il numero {a} è maggiore di {b} e {c}")
    elif b > a and b > c:
        print(f"il numero {b} è maggiore di {a} e {c}")
    elif c > a and c > b:
        print(f"il numero {c} è maggiore di {a} e {b}")
    else:
        print("Sono tutti uguali")
        

a = int(input("a =  "))
b = int(input("b =  "))
c = int(input("c =  "))

trovaIlMassimo(a,b,c)

  