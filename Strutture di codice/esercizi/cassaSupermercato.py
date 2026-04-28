import time
from tqdm import tqdm

prezzoPerSconto = float(50)

while True:
    TotPrezzo = float(0)
    numeroProdotti = int(input("Prodotti: "))
    
    for x in range(0, numeroProdotti):
        prezzo = float(input(f">prezzo prodotto{x+1} "))
        TotPrezzo+=prezzo
        print(TotPrezzo)
        
    if numeroProdotti == 0:
        for i in tqdm(range(10), desc="Chiusura operazione"):
            time.sleep(0.30)
        break
    
    if TotPrezzo > prezzoPerSconto:
        print("Sconto del 10%")
        sconto = TotPrezzo*0.10
        prezzoPerSconto = TotPrezzo - sconto
        print(f"prezzo scontato a {prezzoPerSconto} invece che {TotPrezzo}")
        
    if (TotPrezzo >= 20.0) and (TotPrezzo <= 50.0):
        print("prezzo nella media")
        
    if TotPrezzo <= 20:
        print("Spesa minima")