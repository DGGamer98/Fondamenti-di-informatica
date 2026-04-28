C = 14 
counter = 0

while True:
    numeroTrovato = int(input("Inserisci numero: "))
    counter+=1
    if numeroTrovato == C:
        print("Numero trovaro")
        break
    elif numeroTrovato > C:
        print("numero alto")
    elif numeroTrovato < C:
        print("Numero basso")
    print(f"Numero tentativi fatti {counter}")

    
        