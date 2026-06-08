'''Data la lista ["Roma", "Milano", "Napoli", "Torino"], crea una tupla contenente la lunghezza di ogni città'''


lista_città = ["Roma", "Milano", "Napoli", "Torino"]

lunghezza = tuple(len(x) for x in lista_città)

print(lunghezza)