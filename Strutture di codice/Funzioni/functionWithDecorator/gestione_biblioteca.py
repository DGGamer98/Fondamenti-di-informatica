listbook = []
list_Borrowed_books = []

''' Funzioni di supporto '''

def log_operazione(funzione):
    def wrapper (*args, **kwargs):
        print(f"[LOG] operazione in corso {funzione.__name__}")
        result = funzione(*args, **kwargs)
        print("[LOG] operazione riuscita")
        return result
    return wrapper

def controlla_lista_vuota(funzione):
    def wrapper(*args, **kwargs):
        lista = args[0] #Primo argomento sempre la lista parto dalla posizione 0
        if len(lista) == 0:
            print("Lista vuota")
            return
        return funzione(*args, **kwargs)
    return wrapper


'''Fuzioni per operazioni'''

@log_operazione
def aggiungi_libro(titolo, autore, disponibile):
    global libro
    libro = [titolo, autore, disponibile]
    listbook.append(libro)
    return aggiungi_libro

@log_operazione
@controlla_lista_vuota
def mostra_libri(libri):
    for x in libri:
        print(x)
    return mostra_libri

#toglie un libro dalla lista
@log_operazione
@controlla_lista_vuota
def prendi_libro(libri, titolo):
    for libro in libri:
        # libro è una lista tipo ["Titolo", "Autore", True]
        if libro[0] == titolo:
            list_Borrowed_books.append(libro) # Aggiungi l'intera info del libro
            libri.remove(libro)               # Rimuovilo dai disponibili
            print(f"[LOG] '{titolo}' aggiunto ai libri prestati")
            return # Esci dalla funzione una volta trovato
            
    # Se il ciclo finisce senza 'return', il libro non c'è
    print(f"[ERROR] Il libro '{titolo}' non è presente")

    

while True:
    print("1 aggiungi libro")
    print("2 mostra libri")
    print("3 prendi libro")
    
    scelta = int(input("> "))
    
    if scelta == 1:
        aggiungi_libro(titolo="DivinaCommedia",autore="Dante Alighieri",disponibile=True)
    elif scelta == 2:
        mostra_libri(listbook)
    elif scelta == 3:
        prendi_libro(listbook, titolo="DivinaCommedia")
    elif scelta == 0:
        break
