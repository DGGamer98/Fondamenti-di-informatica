'''Scrivi un programma che legga il contenuto di un file di testo e lo copi in un altro file.'''

path_input = "/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/esercizi/esercizio3/input.txt"
path_output = "/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/esercizi/esercizio3/output.txt"

#lettura file input
with open(path_input, "r", encoding="utf-8") as file_input:
    testo_input = file_input.read()

#scrivo il file input in output
with open(path_output, "a", encoding="utf-8") as file_output:
    testo_output = file_output.write(testo_input)

#leggo il contenuto del file output
with open(path_output, "r", encoding="utf-8") as lettura:
    let = lettura.read()

print(let)