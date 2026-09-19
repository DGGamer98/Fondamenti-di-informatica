s = "Fondamenti2024 Di anna INFOrmatica@Python"

def conta_caratteri(s):
    #variabili contatori
    maiuscole = 0
    minuscole = 0
    numeri = 0
    speciali = 0

    #conto se ci sono lettere
    for x in s:
        if x.isupper():
            maiuscole+=1
        elif x.islower():
            minuscole+=1
        elif x.isdigit():
            numeri+=1
        elif not x.isalnum():
            speciali+=1
    #stampo tutte le lettere
    for x in s:
        print(x)

    return f"Maiuscole {maiuscole}, minuscole {minuscole}, numeri {numeri}, speciali {speciali}"


def is_Polidroma(s):
    stringa_inversa = s[::-1]
    #le rendo delle liste per confrontare gli indici
    list_inversa = stringa_inversa.split()
    s_inversa = s.split()

    for index in list_inversa:
        for index_s in s_inversa:
            if index == index_s:
                return f"parola polidroma: {index}"

    return False

def parole_con_numero(s):
    new_s = s.split()
    new_list = []

    for index in new_s:
        if index.isalnum() and not index.isalpha():
            new_list.append(index)

    return new_list

#TODO Da vedere stasera
def sostituisci_vocali(s):
    for x in s:
        if x == "a" or x == "A":
            x = "*"
        elif x == "e" or x == "E":
            x = "*"
        elif x == "i" or x == "I":
            x = "*"
        elif x == "o" or x == "O":
            x = "*"
        elif x == "u" or x == "U":
            x = "*"
    return s

print("=== conta caratteri ===")
print(conta_caratteri(s))

print("=== polidroma ===")
print(is_Polidroma(s))

print("=== parole_con_numero ===")
print(parole_con_numero(s))

print("=== sotituisci voali ===")
print(sostituisci_vocali(s))