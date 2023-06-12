# Calcolatrice in python

valori = []  # Lista per memorizzare i valori

while True:
    valore = input("Inserisci un valore numerico (o 'q' per visualizzare i risultati): ")
    
    if valore == 'q':
        break  # Esce dal ciclo se l'utente inserisce 'q'
    
    try:
        valori.append(float(valore))  # Tenta di convertire il valore in float e aggiungerlo alla lista
    except ValueError:
        print("Errore: Inserisci solo valori numerici!")

print("Risultati:")
if len(valori) > 0:
    somma = sum(valori)

    sottrazione = valori[0] - sum(valori[1:])

    moltiplicazione = 1
    for valore in valori:
        moltiplicazione *= valore

    divisione = valori[0]
    for valore in valori[1:]:
        divisione /= valore
        
    modulo = valori[0] % valori[1]

    print("Somma:", somma)
    print("Sottrazione:", sottrazione)
    print("Moltiplicazione:", moltiplicazione)
    print("Divisione:", divisione)
    print("Modulo:", modulo)
else:
    print("Nessun valore inserito.")
