voti = []


def media(voti):
    couter = 0
    for voto in voti:
        voto+=voto
        couter = couter + 1
    try:
        mediaTot = voto/couter    
        return mediaTot
    except ZeroDivisionError:
        return "Attenzione divisione per 0"

def voto_massimo(voti):
    votomax = voti[0]
    for x in voti:
        if x > votomax:
            votomax = x
    return votomax

def voto_minimo(voti):
    votomin = voti[0]
    for x in voti:
        if x < votomin:
            votomin = x  
    return votomin

def promosso(mediaTot):
    if mediaTot >= 6:
        print("Studente promosso")
    elif mediaTot <= 5:
        print("Studente bocciato")
        


insertVoto = int(input("Quanti voti inserire? "))

for voto in range(0, insertVoto):
    voto = int(input(f"voto {voto+1}: "))
    voti.append(voto)
    
print("Media: ", media(voti))
print("Voto massimo:", voto_massimo(voti))
print("Voto minimo:", voto_minimo(voti))
print("Promosso:", promosso(media))
