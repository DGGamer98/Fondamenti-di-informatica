def print_perfetti(n):
    '''Stampa i numeri perfetti fino ad n'''
    for i in range(2, n + 1):
        somma = 0
        for y in range(1, i // 2 + 1): #Oltre la metà + 1 non ci sono divisori
            if i % y == 0:
                somma += 1 #Aggiungo a Somma il divisore trovato
                
            if somma == i:
                print(i, end="")
            