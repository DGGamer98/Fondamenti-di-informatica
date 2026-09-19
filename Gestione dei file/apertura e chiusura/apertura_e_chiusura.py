#file_prova = open("/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/file-prova.txt", 'w')

with open("/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/file-prova.txt", "rt") as f:
    file = f.read()
    print(file)