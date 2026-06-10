# ESERCIZIO 1 — global
x = 10

def modifica_x():
    # fai in modo che questa funzione modifichi la x globale
    # dopo la chiamata x deve essere 99
    global x
    x = 99

modifica_x()
print(x)  # deve stampare 99


# ESERCIZIO 2 — nonlocal
def contatore():
    count = 0
    def incrementa():
        # fai in modo che questa funzione incrementi count
        # usa nonlocal
        nonlocal count
        count+=1
    incrementa()
    incrementa()
    incrementa()
    print(count)  # deve stampare 3

contatore()


# # ESERCIZIO 3 — LEGB completo
# x = "globale"

# def esterna():
#     x = "esterna"
#     def interna():
#         # quale x vede questa funzione?
#         # prova a stampare x senza modificarla
#         # poi prova a modificarla con nonlocal
#         pass
#     interna()
#     print(x)

# esterna()
# print(x)