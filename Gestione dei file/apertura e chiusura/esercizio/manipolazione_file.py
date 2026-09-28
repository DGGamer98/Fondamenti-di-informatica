with open("/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/esercizio/input.txt", "r") as f1, \
    open("/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/esercizio/output.txt", "w") as f2:

    lines = f1.readlines()

    flags = True
    counter = 1

    for line in lines:
        if counter %2 != 0:
            outputFile = f2.write(f"{counter}: {line}")
            
    