'''
1️⃣ Traccia: Sistema Ospedale Veterinario
Contesto: Gestisci una clinica veterinaria con animali, proprietari e veterinari.
Entità del sistema:
Una Persona come classe base. Un Proprietario che porta gli animali. Un Veterinario che visita gli animali. Un Animale con una sua cartella clinica. Una Clinica che coordina tutto.
Relazioni richieste:

Almeno una ereditarietà
Almeno una composizione
Almeno una aggregazione
Almeno una associazione

Vincoli semantici con @property:

L'età del proprietario deve essere tra 18 e 90
Il peso dell'animale deve essere maggiore di 0
Un proprietario può avere massimo 4 animali registrati

Eccezioni da gestire:

Animale non trovato
Troppi animali registrati
Età non valida
Peso non valido
Clinica al completo

Test con unittest:

test_eta_valida — assertEqual
test_eta_non_valida — assertRaises
test_visita_ok — assertTrue
test_troppi_animali — assertRaisesRegex
test_peso_non_valido — assertRaises
'''