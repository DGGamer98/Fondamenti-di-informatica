# apre DUE file contemporaneamente con un solo with
# f_in → file di input (rt = read text)
# f_out → file di output (w = write)
with open("isolamisteriosa.txt", "rt") as f_in, \
     open("outputfile.txt", "w") as f_out:

    # legge TUTTE le righe di f_in in una lista
    # es. lines = ["riga1\n", "riga2\n", "riga3\n", ...]
    lines = f_in.readlines()

    flag = True    # interruttore on/off
    counter = 1    # conta le righe scritte

    for line in lines:
        if flag == True:          # se flag è True → scrivi la riga
            f_out.write(f"{counter}: {line}")  # scrive "1: riga1"
        
        flag = not flag    # inverte flag: True→False→True→False...
        counter += 1       # incrementa sempre il contatore