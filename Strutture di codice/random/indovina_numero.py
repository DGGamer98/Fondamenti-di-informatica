import random

MAX_TENTAVIVI = 3
n_da_indovinare = random.randint(1,100)
indovinato = False
tenativi = 1 #Conto i tentativi

while not indovinato and tenativi <= MAX_TENTAVIVI:
    prompt = "Tentativo" + str(tenativi) + ") numero: "
    n = eval(input(prompt))
    
    #vari controlli per il gioco
    if n_da_indovinare == n:
        print("\n complimenti")
        indovinato = True #prossimo controllo python esce dall'iteratore
    elif n > n_da_indovinare:
        print("Ho pensato un numero più piccolo\n")
    else:
        print("Ho pensato a un numero più grande\n")
        
    tenativi +=1
    
if not indovinato:
    print("Avevo pensato il numero", n_da_indovinare)
    print("Ritenta sarai più fortunato")
    