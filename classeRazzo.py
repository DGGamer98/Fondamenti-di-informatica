import time

class Razzo:

    #Attributi di classe
    agenzia = "Telespazio"
    contatore = 0

    #costruttore, attributi di istanza
    def __init__(self, nome, tipo):
        Razzo.contatore+=1
        self.nome = nome
        self.tipo = tipo
        self.stato = "pronto"
        self.carburante = 100
        self.payload = []

    def aggiungi_payload(self, satellite):
        if self.stato == "in preparazione":
            print("[LOG] non puoi aggiungere payload!")
            return
        elif satellite in self.payload:
            print("[LOG] satellite già presente nella lista")
            return

        scelta = input("vuoi aggiungere dei satelliti? yes or no ")

        #Condizione per aggingere satelliti al razzo --> max 3
        if scelta == "yes":
            for satellite in range(0,3):
                satellite = input(f"satellite {satellite+1} ")
                self.payload.append(satellite)
                print("[LOG satellite aggiunto]")
        elif scelta == "No":
            return
    
    #check per controllare la quantita
    def rifornisci(self, quantita):
        if quantita == self.carburante:
            print("[LOG] Serbatoio già pieno")
        elif quantita > self.carburante:
            print("[ERROR] impossibile superare 100")
        elif self.carburante < quantita:
            self.carburante+=quantita
            print("[LOG] carburante aggiunto")


    def segna_pronto(self):
        #codice per trovare il singolo elemento nella lista
        for payload in self.payload:
            if payload in self.payload:
                self.stato = "pronto"
                print("[LOG stato cambiato]")
            else:
                print("[LOG] Nessun payload trovato")
                break

    def lancia(self):
        if self.stato != "pronto":
            print("[LOG] Razzo non pronto al lancio")
        else:
            for i in range(10, 0, -1):
                print(i)
                time.sleep(0.5)
            print("Lancio :) ")

    def __str__(self):
        listaUnion = ", ".join(self.payload)
        return f"| Nome: {self.nome} | Tipo: {self.tipo} | Stato: {self.stato} | Carburante: {self.carburante} | Payload: {listaUnion}"
    

s1 = Razzo("vega-c","europeo")
s1.aggiungi_payload("prisma")
s1.rifornisci(50)
s1.lancia()
