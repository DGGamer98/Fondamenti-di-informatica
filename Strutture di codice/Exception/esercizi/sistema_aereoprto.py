'''TODO Davide
Esercizio 3 — Medio (solo traccia): Sistema Aeroporto 
Contesto: Devi progettare un sistema di gestione per un aeroporto che gestisce voli, passeggeri e gate.
Requisiti del sistema:
Il sistema deve modellare le seguenti entità: 

un Passeggero con nome, codice fiscale e bagagli; 
un Volo che ha un numero di volo, destinazione, capienza massima e lista passeggeri; 
un Gate che gestisce i voli assegnati; 
un Aeroporto che coordina tutto.

Relazioni richieste:

Deve essere presente almeno una ereditarietà
Deve essere presente almeno una composizione
Deve essere presente almeno una aggregazione
Deve essere presente almeno una associazione

Eccezioni da gestire:

Volo pieno quando si cerca di aggiungere un passeggero oltre la capienza
Passeggero già presente nel volo
Gate non disponibile
Bagaglio troppo pesante (limite 23kg)
Volo non trovato quando si cerca per numero

Decorator richiesti:

Uno di log con timestamp
Uno di validazione

Il sistema deve permettere di:

Aggiungere passeggeri a un volo
Assegnare un volo a un gate
Fare il check-in di un passeggero
Stampare il report completo dell'aeroporto
Cercare un volo per numero
'''
class Gate():
    def __init__(self, codiceGate, lato, nomeGate):
        self.codiceGate = codiceGate
        self.nomeGate = nomeGate
        self.lato = lato
        self.voliAssegnati = [] #lista di oggetti
    
    #Aggregazione gate a dei voli i voli esistono anche senza gate, di base usiamo l'associazione
    def assegnaVoli(self, voli):
        self.voliAssegnati.append(voli)
        print(f"[LOG] volo assengato al gate {self.nomeGate} codiceGate: {self.codiceGate}")

    def __str__(self):
        voli_str = ", ".join(str(v) for v in self.voliAssegnati)  # converte ogni oggetto
        return f"| Nome gate: {self.nomeGate} | Codice Gate: {self.codiceGate}, | lato: {self.lato} | voli gate {voli_str}"
    
class Aereoporto():
    def __init__(self, nome, numeroPiste):
        self.nome = nome
        self.numeroPiste = numeroPiste
        self.numeroGate = [Gate(f"G{i+1}", "A", f"Gate {i+1}") for i in range(numeroPiste)] #Composizione --> inizializzo gate, se aereoporto decate crollano anche i gate

    def __str__(self):
        return f"Aeroporto: {self.nome} | Piste: {self.numeroPiste} | Gate: {len(self.numeroGate)}"

class Passeggero:
    def __init__(self, nome, codiceFiscale, bagagli):
        self.nome = nome
        self.codiceFiscale = codiceFiscale
        self.bagagli = bagagli

    def assegnazioneGate(self, gate): #Associazione ---> uso class gate
        print(f"Il passeggero {self.nome} è stato assegnato il gate {gate}")

    def __str__(self):
        return f"Scheda passeggero/a | nome: {self.nome} | codice fiscale: {self.codiceFiscale} | numero bagagli: {self.bagagli} "
    
class Voli:
    def __init__(self, numeroVolo, destinazione, capienza_massima):
        self.numeroVolo = numeroVolo
        self.destinazione = destinazione
        self.capienza_massima = capienza_massima
        self.lista_passeggeri = []

    #Passo l'istanza di passeggeri come parametro in ingresso 
    def add_passeggeri(self, passeggeri):
        self.lista_passeggeri.append(passeggeri)
        print("[LOG] passeggero aggiunto")

    def __str__(self):
        passeggeri = ", ".join(str(v) for v in self.lista_passeggeri)
        return f"Scheda voli: | numero volo {self.numeroVolo} | destinazione {self.destinazione} | capienza massima {self.capienza_massima} | lista passeggeri: {passeggeri}"

    
    
    

#TODO Execution testing for the task on python.   


passeggero1 = Passeggero("Davide", "DVDFDF99D99D99D9", 2)
gate1 = Gate("A1", "sinistro", "Gate A1")
Aereoporto1 = Aereoporto("Fiumicino", 3)
voli1 = Voli("rt-b34","Stati Uniti",120)

print(passeggero1)
print(Aereoporto1)
print(voli1)

#TODO aggiungere dei voli al gate
passeggero1.assegnazioneGate(gate1) #Associativa
gate1.assegnaVoli(voli1)

print(gate1)

voli1.add_passeggeri(passeggero1)
print(voli1)
