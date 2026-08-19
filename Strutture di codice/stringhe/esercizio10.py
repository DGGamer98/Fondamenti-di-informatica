testo = "Telespazio 2024: Lanciamo 3 Satelliti in Orbita GEO!"

#variabili globali
Maiuscolo = 0
Minuscolo = 0
Numeri = 0
Caratteri_speciali = 0

def analizza_testo(testo):
    for x in testo:
        if x.isupper():
            global Maiuscolo
            Maiuscolo+=1
        elif x.islower():
            global Minuscolo
            Minuscolo+=1
        elif x.isdigit():
            global Numeri
            Numeri+=1
        elif not x.isalnum():
            global Caratteri_speciali
            Caratteri_speciali+=1

    return f"il testo contiene {Maiuscolo} lettere maiuscole, {Minuscolo} lettere minuscole, ed anche {Numeri} numeri ed infine {Caratteri_speciali} caratteri speciali"


def parola_più_lunga(testo):
    testo_diviso = testo.split()
    valore_iniziale = testo_diviso[0]

    for parola in testo_diviso:
        # Confrontiamo la lunghezza della parola corrente con quella massima
        if len(parola) > len(valore_iniziale):
            valore_iniziale = parola

    return f"la parola più lunga è {valore_iniziale}"


def conta_vocali(testo):
    counter = 0
    for vocale in testo:
        if (vocale.count("a")) or (vocale.count("A")):
            counter+=1
        elif (vocale.count("e")) or (vocale.count("E")):
            counter+=1
        elif (vocale.count("i")) or (vocale.count("I")):
            counter+=1
        elif (vocale.count("o")) or (vocale.count("O")):
            counter+=1
        elif (vocale.count("u")) or (vocale.count("U")):
            counter+=1

    return f"Vocali trovati {counter}"


def censura(testo, parola):
    parola_divisa = testo.split()
    counter = 0
    for x in parola_divisa:
        if parola == x:
            parola_divisa[counter] = "****"
        counter+=1

    newString = " ".join(parola_divisa)
    return newString

print("=== analisi testo ===")
print(analizza_testo(testo))

print("=== parola più lunga ===")
print(parola_più_lunga(testo))

print("=== conta vocali ===")
print(conta_vocali(testo))

print("=== censura ===")
print(censura(testo, "Satelliti"))