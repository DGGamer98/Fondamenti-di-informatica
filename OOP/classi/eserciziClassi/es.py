# ============================================
# ASSOCIAZIONE — Medico "usa" Paziente
# I due oggetti esistono indipendentemente
# ============================================

class Paziente:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def visitato(self, medico):
        print(f"{self.nome}, eta {self.eta} viene visitato da {medico.nome}")

class Medico:
    def __init__(self, nome):
        self.nome = nome

    def visita(self, paziente): # riceve Paziente dall'esterno
        print(f"{self.nome} visita {paziente.nome} ({paziente.eta} anni)")
         # se cancello il Medico, il Paziente esiste ancora → ASSOCIAZIONE

# ============================================
# AGGREGAZIONE — Reparto "ha" dei Medici
# I Medici esistono anche senza il Reparto
# ============================================

class Repato:
    def __init__(self, nome):
        self.nome = nome
        self.medici = []

    def aggiungi_medico(self, medico):
        self.medici.append(medico)
        print(f"{medico.nome} aggiunto al reparto {self.nome}")

    def mostra_medici(self):
        for m in self.medici:
            print(f"  - {m.nome}")

# ============================================
# COMPOSIZIONE — Paziente "possiede" CartellaClinica
# La cartella non esiste senza il Paziente
# ============================================

class CartellaClinica:
    def __init__(self):
        self.diagnosi = []

    def aggiungi_diagnosi(self, d):
        self.diagnosi.append(d)

    def mostra(self):
        for d in self.diagnosi:
            print(f"  - {d}")

class PazienteCompleto:
    def __init__(self, nome):
        self.nome = nome
        self.cartella = CartellaClinica()  # creata DENTRO → COMPOSIZIONE