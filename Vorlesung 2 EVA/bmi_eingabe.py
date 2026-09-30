# E = Eingabe
weight = int(input("Bitte das Gewicht in kg eingeben: "))   # Masse in kg
height = input("Bitte die Größe in cm eingeben: ")  # Größe in cm

# Typumwandlung
height = int(height)

# V = Verarbeitung
bmi = weight/((height/100)**2) # Berechnung Body-Mass-Index

# A = Ausgabe
print("BMI = ", bmi)
