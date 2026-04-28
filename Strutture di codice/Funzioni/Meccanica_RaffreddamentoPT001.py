from tqdm import tqdm
import time

listTemperatura = []

def accettazioneTemp(valueTemp):
    if(valueTemp >= 2) and (valueTemp <=8):
        print("Temperatura sotto la norma")
        listTemperatura.append(valueTemp)
    else:
        print("Allarme")
        

while True:
    user_add = input("Vuoi conttrollare la temperatura? yes or stop: ")
    
    if user_add =='yes':
        try:
            valueTemp = int(input("Inserisci temperatura: "))
            accettazioneTemp(valueTemp)
        except ValueError:
            print("Errore dei inserire un numero intero")
            
    elif user_add == 'stop':
        for x in tqdm(range(10), desc="Uscita in corso"):
            time.sleep(0.30)
        break
            
for temp in listTemperatura:
    print(temp)