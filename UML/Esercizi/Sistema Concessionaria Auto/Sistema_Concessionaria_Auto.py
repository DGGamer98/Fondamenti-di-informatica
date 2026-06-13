'''Traccia: Sistema Concessionaria Auto
Contesto: Progetta un sistema per gestire una concessionaria con auto, clienti e venditori.
Entità del sistema:

Una Persona come classe base. Un Cliente che acquista o noleggia auto. Un Venditore che gestisce le vendite. Un'Auto con una sua scheda tecnica. Una Concessionaria che coordina tutto.
Relazioni richieste:

Almeno una ereditarietà
Almeno una composizione
Almeno una aggregazione
Almeno una associazione

Vincoli semantici con @property:

L'età del cliente deve essere tra 18 e 100
Il prezzo dell'auto deve essere maggiore di 0
Un cliente può prenotare massimo 2 test drive contemporaneamente

Eccezioni da gestire:

Auto non disponibile
Auto non trovata
Età non valida
Troppi test drive prenotati
Concessionaria al completo

Decorator richiesti:

Uno di log con timestamp
Uno che controlla che l'auto sia disponibile prima del test drive

Il sistema deve permettere di:

Aggiungere auto e clienti alla concessionaria
Prenotare un test drive
Vendere un'auto
Cercare un'auto per modello
Stampare il report completo

Test con unittest:

test_eta_valida — assertEqual
test_eta_non_valida — assertRaises
test_test_drive_ok — assertTrue
test_auto_non_disponibile — assertRaises
test_troppi_test_drive — assertRaisesRegex'''