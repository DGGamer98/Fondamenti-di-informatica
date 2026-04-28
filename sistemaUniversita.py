import random

# COMPOSIZIONE — Libretto appartiene allo Studente  
class Libretto:
    def __init__(self):
        self.voti = []

    def aggiungi_voto(self, materia, voto):
        voti = {
            "materia": materia,
            "voto": voto
        }

        self.voti.append(voti)
        print("[LOG] voto aggiunto")

    def calcolo_media(self):
        counter = 0 

        if len(self.voti) == 0: #controllo che la lisa non sia vuota
            print("[LOG] la lista è vuota")
        else:
            for x in self.voti:
                counter += 1
                totaleVoti=+x["voto"]
                media = totaleVoti/counter
            return media
    
    def mostra(self):
        for x in self.voti:
            print(x)
        
class Persona: #EREDITARIETÀ
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def __str__(self):
        return f"nome: {self.nome} eta: {self.eta}"

class Studente(Persona):
    counter = 0

    def __init__(self, nome, eta):
        super().__init__(nome, eta)
        self.matricola = f"MAT-{random.randint(1000, 9999)}"
        self.libretto = Libretto()
        self.stato = "iscritto"

    def __str__(self):
        return f" | Nome {self.nome} | eta {self.eta} | matricola {self.matricola} | media {self.libretto.calcolo_media()}"

class Professore(Persona):
    def __init__(self, nome, materia, eta):
        super().__init__(nome, eta)
        self.materia = materia

    def interroga(self, studente, voto): #ASSOCIAZIONE --> studente
        print(f"| Prof.{self.nome} interroga {studente} in {self.materia} | voto {voto}")
        if voto >= 18:
            studente.libretto.aggiungi_voto(self.materia, voto)
            print(f"[LOG] studente promosso con voto {voto}")
        elif voto < 18:
            print(f"[LOG] lo studente è stato bocciato")

    def __str__(self):
        return f"| Prof. {self.nome} | {self.materia} |"

class Corso:
    def __init__(self, nome):
        self.nome = nome
        self.professori = []
        self.studenti = []

    def aggiungi_professore(self, professore): #AGGREGAZIONE --> professore
        #Controllo se il professore già esiste
        if professore in self.professori:
            print("[LOG] docente già esistente nel corso")

        self.professori.append(professore)
        print("[LOG] professore aggiunto")

    def iscrivi_studente(self, studente): #AGGREGAZIONE --> studente
        if studente in self.studenti:
            print("[LOG] studente già iscritto al corso")

        self.studenti.append(studente)
        print("[LOG] studente aggiunto al corso universitario")

    def mostra_corso(self):
        print(f"Corso {self.nome}")
        #Stampo tutti i docenti
        for professore in self.professori:
            print(professore)

        #Stampo tutti i studenti con la media
        for studente in self.studenti:
            print(studente)

    def studenti_promossi(self):
        for studente in self.studenti:
            if studente[3] >= 18:
                print(studente)
            else:
                return False
        

# crea persone
p1 = Professore("Rossi", "Matematica", 55)
p2 = Professore("Bianchi", 48, "Fisica")
s1 = Studente("Mario", 22)
s2 = Studente("Luigi", 23)

# crea corso e aggiungi (AGGREGAZIONE)
corso = Corso("Ingegneria")
corso.aggiungi_professore(p1)
corso.aggiungi_professore(p2)
corso.iscrivi_studente(s1)
corso.iscrivi_studente(s2)

# interrogazioni (ASSOCIAZIONE)
p1.interroga(s1, 28)
p1.interroga(s1, 30)
p2.interroga(s2, 16)
p2.interroga(s2, 24)

# mostra libretti (COMPOSIZIONE)
print("\n--- Libretto Mario ---")
s1.libretto.mostra()
print(f"Media: {s1.libretto.media()}")

# mostra corso
print("\n--- Corso ---")
corso.mostra_corso()

# promossi
print("\n--- Promossi ---")
corso.studenti_promossi()

# verifica aggregazione
del corso
print(p1)  # esiste ancora!


        
        




