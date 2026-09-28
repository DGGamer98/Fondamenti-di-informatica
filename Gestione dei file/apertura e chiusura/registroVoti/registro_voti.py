class RegistroVoti():
    def __init__(self, nome, voti):
        self.nome = nome
        self.voti = voti

    def leggi_voti(self, nome_file):
        with open(nome_file, "r", encoding="utf-8") as file1:
            lettura = file1.readlines()
            #print(lettura)
            # for x in lettura:
            #     vision = x.split()
            #     print(vision)
            

    def inserisci_voto(self, nome_file):
        with open(nome_file, "+a", encoding="utf-8") as file:
            riga = file.write(f"{self.nome} {(self.voti)}\n")


    def scrivi_promossi(nome_file, output_file):
        with open(nome_file, "r", encoding="utf-8") as f_in, \
            open(output_file, "w", encoding="utf-8") as f_out:  # ← apri anche il file di output
            
            for riga in f_in:
                dati = riga.split()
                nome = dati[0]           # ← prendi il nome
                voto = int(dati[1])      # ← converti il voto in int
                
                if voto >= 6:
                    # ← scrivi nel file di output invece di print!
                    f_out.write(f"{nome}: promosso con voto {voto}\n")




registroVoti = RegistroVoti(nome="Davide", voti=8)

registroVoti.inserisci_voto(nome_file="/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/registroVoti/output.txt")
registroVoti.leggi_voti(nome_file="/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/registroVoti/output.txt")

RegistroVoti.scrivi_promossi(nome_file="/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/registroVoti/output.txt", output_file="/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/registroVoti/superiori_a_6.txt")