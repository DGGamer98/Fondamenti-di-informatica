import random
from tqdm import tqdm
import time

def login(username, password):
    while True:
        insertUser = input("Username: ")
        insertPassword = input("password: ")
        
        if (insertUser == username) and (insertPassword == password):
            generateCode = random.randrange(0,255)
            print(generateCode)
            insertCode = int(input("insert: "))
        
            if insertCode == generateCode:
                for x in tqdm(range(10), desc="Accesso in corso"):
                    time.sleep(0.30)
                print("Accesso acconsentito")
                break
            else:
                print("Insert code errato")
        
        elif (insertUser == username) and (insertPassword != password):
            print("password sbagliata")
        
        elif (insertUser != username) and (insertPassword == password):
            print("username sbagliato")
            

password = "alfa123"
username = input("Nome utente")

login(username, password)