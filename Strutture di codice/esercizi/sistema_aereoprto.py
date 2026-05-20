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
    
    def cerca_voli(self, numeroVolo):
        for volo in self.voliAssegnati:
            if str(volo.numeroVolo) == str(numeroVolo):
                print("volo trovato")
                return volo
            else:
                print("Volo non trovato")
                return None
                
        
    def stampa_lista(self):
        for x in self.voliAssegnati:
            print(x)

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
        if self.bagagli > 23:
            raise ValueError("Bagaglio troppo pesante")
        
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
        
        if len(self.lista_passeggeri) < self.capienza_massima:
                self.lista_passeggeri.append(passeggeri)
                print("[LOG] passeggero aggiunto")
        else:
            raise ValueError ("Errore di capienza")
        
        if passeggeri in self.lista_passeggeri[0:-1]: #Controllo se il passeggero è già presente nella lista, escludendo l'ultimo elemento che è quello appena aggiunto
            raise ValueError("Passeggero già presente nel volo")
        
    def __str__(self):
        passeggeri = ", ".join(str(v) for v in self.lista_passeggeri)
        return f"Scheda voli: | numero volo {self.numeroVolo} | destinazione {self.destinazione} | capienza massima {self.capienza_massima} | lista passeggeri: {passeggeri}"


passeggero1 = Passeggero("Davide", "DVDFDF99D99D99D9", 2)
passeggero2 = Passeggero("Luca", "LCCU23ZB", 1)

gate1 = Gate("A1", "sinistro", "Gate A1")
Aereoporto1 = Aereoporto("Fiumicino", 3)
voli1 = Voli("rt-b34","Stati Uniti",3)

# print(passeggero1)
# print(Aereoporto1)
# print(voli1)

passeggero1.assegnazioneGate(gate1) #Associativa
gate1.assegnaVoli(voli1)

# print(gate1)

voli1.add_passeggeri(passeggero1)
voli1.add_passeggeri(passeggero2)
print(voli1)

gate1.cerca_voli("rt-b34")



