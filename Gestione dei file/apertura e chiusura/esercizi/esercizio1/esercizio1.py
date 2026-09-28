'''Scrivi un programma che legga il contenuto di un file di testo e lo stampi a schermo.'''

path = "/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/esercizi/esercizio1/fileTesto.txt"

with open(path, "r") as file:
    testo = file.read()
    print(testo)