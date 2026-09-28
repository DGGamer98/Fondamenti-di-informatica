with open("/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/Diario_Personale/diario.txt", "w") as f1:
    f1.write("Ho studiato Python\n")
    f1.write("Ho mangiato la pizza\n")
    f1.write("Ho guardato un film\n")

#aggiungiamo una riga senza cancellare le altre 
with open("/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/Diario_Personale/diario.txt", "a+") as f2:
    f2.write("provo file")

#Leggiamo il file numerando le righe

with open("/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/Diario_Personale/diario.txt", "r") as f3:
    file = f3.readlines()
    counter = 1
    for line in file:
        print(f"{counter}: {line}")
        counter+=1

    # for numero, riga in enumerate(f3, start=1):
    #     print(f"{numero}: {riga.strip()}")