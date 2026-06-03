'''
2. Record di un Database (Dati misti ed eterogenei)Puoi usare una tupla per raggruppare informazioni correlate di tipo diverso che descrivono un singolo elemento o utente.
'''

# Record di un prodotto: (ID, Nome, Prezzo, Disponibile)
prodotto = (101, "Tastiera Wireless", 49.99, True)

# Spacchettamento (Unpacking) della tupla in variabili chiare
id_prod, nome, prezzo, disponibile = prodotto

print(f"Il prodotto '{nome}' costa {prezzo}€.")