'''Scrivi un programma che chieda all’utente di inserire una stringa, quindi scriva la stringa in un file di testo..'''

path = "/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/esercizi/esercizio2/test.txt"

# with open(path, "r", encoding="utf-8") as file, \
#     open(path, "a", encoding="utf-8") as fileOutput:

#     testo = input("Inserisci testo > ")
#     fileOutput.write(testo)

#     print(file)

with open(path, "a", encoding="utf-8") as fileOutput:
    testo = input("Inserisci testo > ")
    fileOutput.write(testo)


with open(path, "r", encoding="utf-8") as file:
    testoIput = file.read()


print(testoIput)