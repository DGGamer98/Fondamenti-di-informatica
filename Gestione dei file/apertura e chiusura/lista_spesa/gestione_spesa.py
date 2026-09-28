with open("/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/lista_spesa/lista.txt", "a+") as f1:
    riga1 = f1.write("biscotti\n")
    riga2 = f1.write("Mozzarella\n")

#leggiamo il file e numeriamo l'output
def lettura():
    with open("/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/lista_spesa/output.txt", "w") as f2, \
        open("/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/lista_spesa/lista.txt") as f1:
        counter = 1
        for line in f1:
            f2.write(f"{counter}: {line}")
            counter+=1
        # for numero, line in enumerate(f1, start=1):
        #     f2.write(f"{numero}: {line.strip()}")


def conta_prodotti(name_file):
    with open("/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/lista_spesa/output.txt") as file:
        righe = file.readlines()
        return len(righe)
    

lettura()
print(conta_prodotti(name_file="/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/lista_spesa/output.txt"))


