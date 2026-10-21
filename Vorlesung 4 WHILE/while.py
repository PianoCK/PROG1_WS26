import random
spiel = True
while spiel:
    zahl1 = random.randint(1,10)
    zahl2 = random.randint(1,10)
    summe = zahl1 + zahl2
    abbruch = False

    for versuch in 1, 2, 3:
        frage = f"Versuch {versuch}: Was ist {zahl1} + {zahl2} ? "
        try:
            tipp = int(input(frage)) # Hier hat die Typumwandlung geklappt
        except:
            abbruch = True # Falls keine Zahl eingeben wurde, dann Abbruch!

        if summe == tipp and not abbruch: # Solange kein Abbruch ist, versuche Lösung
            print("Richtige Antwort")
            break
        else:
            print("Das war falsch")
    weiter = input("Möchtest Du nochmal spielen? (J/N)")
    if weiter != "J":
        spiel = False

print("Programmende")
