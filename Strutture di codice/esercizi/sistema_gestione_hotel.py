'''TODO Traccia task esercizio ESAME

Traccia: Sistema di gestione hotel
Contesto: Devi progettare un sistema per la gestione di un hotel che gestisce camere, ospiti e prenotazioni.
Entità del sistema:
Un Ospite con nome, età e documento d'identità. Una Camera con numero, tipo e prezzo per notte. Una Prenotazione che collega un ospite a una camera con date di check-in e check-out. Un Hotel che coordina tutto.
Relazioni richieste:

Almeno una ereditarietà
Almeno una composizione
Almeno una aggregazione
Almeno una associazione

Vincoli semantici con @property:

L'età dell'ospite deve essere tra 18 e 100
Il prezzo per notte deve essere maggiore di 0
Il tipo di camera deve essere uno tra: "singola", "doppia", "suite"
Il numero di camera deve essere maggiore di 0

Eccezioni da gestire:

Camera già occupata
Ospite già registrato
Date non valide (check-out prima di check-in)
Documento d'identità non valido (meno di 5 caratteri)
Hotel al completo

Decorator richiesti:

Uno di log con timestamp
Uno che controlla che la camera sia disponibile prima di prenotare

Il sistema deve permettere di:

Registrare un ospite
Prenotare una camera
Fare il check-in e check-out
Stampare il report completo dell'hotel con camere libere e occupate'''