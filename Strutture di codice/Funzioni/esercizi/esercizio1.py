'''Scrivi una funzione che prende una lista di numeri e restituisce la somma di tutti gli elementi.'''
num_list = [10, 20, 30]

def somma_Lista(lista):
    num = 0
    for x in lista:
        num+=x
    return num
    
print(somma_Lista(num_list))