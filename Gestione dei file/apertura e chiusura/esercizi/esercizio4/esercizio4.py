path_input = "/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/esercizi/esercizio4/input.txt"
path_output = "/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/esercizi/esercizio4/output.txt"
# Apri il file in modalità lettura
with open(path_input, 'r') as file, \
    open(path_output, "w") as output_file:
    # Conta le righe utilizzando una list comprehension per leggere il file
    #numero_righe = sum(1 for line in file)
    counter = 0
    for line in file:
        counter+=1
        output_file.write(f"{counter} {line}")

# Stampa il numero totale di righe nel file
print(f"Il file contiene {counter} righe.")