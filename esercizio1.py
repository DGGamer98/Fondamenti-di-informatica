# COMPOSIZIONE — CartellaClininca appartiene al Paziente
class CartellaClinica:
    def __init__(self):
        self.diagnosi = []

    def aggiungi_diagnosi(self, diagnosi):
        self.diagnosi.append(diagnosi)

    def mostra(self):
        for diagnosi in self.diagnosi:
            print(diagnosi)

# COMPOSIZIONE + EREDITARIETÀ
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def __str__(self):
        return f"nome {self.nome} eta {self.eta}"
    

class Paziente(Persona): # EREDITARIETÀ da Persona
    def __init__(self, nome, eta, codice):
        super().__init__(nome, eta)
        self.codice = codice
        self.cartella = CartellaClinica() # composizione --> inizializzo la classe nella padre paziente
        self.stato = "ricoverato"

    def dimetti(self):
        self.stato = "Dimesso"

    def __str__(self):
        return f"| {self.nome} | {self.eta} | {self.codice}"
    

class Medico(Persona):  # EREDITARIETÀ da Persona
    def __init__(self, nome, eta, specializazzioni):
        super().__init__(nome, eta)
        self.specializazzioni = specializazzioni

    def visita(self, paziente): # ASSOCIAZIONE — usa Paziente
        print(f"il dott. {self.nome} visita il {paziente}")

    def __str__(self):
        return f"dott. {self.nome} | specializato in {self.specializazzioni}"
    

class Reparto(): # AGGREGAZIONE — Reparto ha Medici e Pazienti
    def __init__(self, nome):
        self.nome = nome
        self.medici = []
        self.pazienti = []

    def aggiungi_medico(self, medico):
        self.medici.append(medico)

    def aggiungi_paziente(self, paziente):
        self.pazienti.append(paziente)

    def mostra_reparto(self):
        print(f"Nome reparto {self.nome}")

        for medico in self.medici:
            print(medico)

        for paziente in self.pazienti:
            print(paziente)

    def dimetti(self, nome):
        if nome in self.pazienti:
            Paziente.dimetti()
            self.pazienti.remove(nome)


# crea persone
m1 = Medico("Rossi", 50, "Cardiologia")
m2 = Medico("Bianchi", 45, "Neurologia")
p1 = Paziente("Mario", 65, "PAZ-001")
p2 = Paziente("Luigi", 40, "PAZ-002")

# crea reparto e aggiungi (AGGREGAZIONE)
reparto = Reparto("Cardiologia")
reparto.aggiungi_medico(m1)
reparto.aggiungi_medico(m2)
reparto.aggiungi_paziente(p1)
reparto.aggiungi_paziente(p2)

# visite (ASSOCIAZIONE)
m1.visita(p1)
m2.visita(p2)

# mostra cartelle
print("\n--- Cartella di Mario ---")
p1.cartella.mostra()

# mostra reparto
print("\n--- Reparto ---")
reparto.mostra_reparto()

# dimetti
reparto.dimetti_paziente("Mario")
print(p1)  # stato aggiornato?

# verifica aggregazione
del reparto
print(m1)  # esiste ancora!