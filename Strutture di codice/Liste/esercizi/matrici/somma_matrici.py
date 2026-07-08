'''
Obiettivo: creare una matrice e calcolare la somma di tutti i suoi elementi.

Consegna:

Crea una matrice 3×3 usando una lista di liste.
Scrivi un programma che calcoli la somma di tutti gli elementi.
Stampa il risultato.
'''

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]



def somma(matrice):
    counter_element = 0 #variabile contatore

    for i in matrice:
        for j in i:
            counter_element+=j
    return counter_element


risultato = somma(matrice)

print(f"La somma della matrice è {risultato}")
