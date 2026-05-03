class SaldoInsufficienti(Exception):
    pass

class ImportoNonValido(Exception):
    pass

class ContoChiuso(Exception):
    pass



class contoBancario:
    banca = "banca d'italia"
    counter = 0

    def __init__(self, titolare):
        contoBancario.counter+=1
        self.titolare = titolare
        self.saldo = 0
        self.attivo = False
        self.iban = f"IT{contoBancario.counter:04b}"
        self.storico = []

    #Metodo per depositarte
    def deposita(self, importo):
        if importo <= 0:
            raise ImportoNonValido("Importo non valido")
        elif self.attivo == False:
            raise ContoChiuso("Il conto non è attivo")
        else:
            self.saldo += importo
            totImporto = f"Deposito {importo}"
            self.storico.append(totImporto)
            print("[LOG] transazione approvata")

    #Metodo per prelevare
    def preleva(self, importo):
        if importo > self.saldo:
            raise SaldoInsufficienti("Il saldo non è sufficiente")
        elif self.attivo == False:
            raise ContoChiuso("Il conto non è attivo")
        elif importo <= 0:
            ImportoNonValido("Impossible prelevare 0 euro")
        else:
            self.saldo-=importo
            totPrelievo = f"Prelievo {importo}"
            self.storico.append(totPrelievo)
            print("[LOG] prelievo avvenuto")

    #Funzioni di supporto    
    def Storico(self):
        for x in self.storico:
            print(x)

    def saldoDispnibile(self):
        print(f"saldo disponibile: {self.saldo}")

    #Formatto il risultato del print
    def __str__(self):
        return f"Titolare: {self.titolare} | Saldo: {self.saldo} | Iban:  {self.iban} | Storico: {self.storico}"

s1 = contoBancario("Davide")
s1.deposita(100)
s1.saldoDispnibile()
s1.preleva(50)
s1.saldoDispnibile()
s1.Storico()

print(s1)




