'''L'utente deve continuare a inserire dei caratteri fino a che non inserisce uno dopo l'altro due caratteri consecutivi.
ad esempio si ferma dopo aver letto uno dopo l'altro 'a' e 'b' '''

alfabeto = "abcdefghijklmnopqrstuvwxyz"
precedente = ""

while True:
    char = input("Inserisci caratteri: ")
    
    #controllo se il carattere attuale è il successivo di quello precedente
    if len(precedente) > 0 and ord(char) == ord(precedente) + 1:
        print(f"Hai inserito due caratteri consecutivi: {precedente} e {char}")