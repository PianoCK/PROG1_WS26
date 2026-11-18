# Telefonnummer-Liste -> index:value --> O(n)
telefonnummern = []
telefonnummern.append(["Joey", "0151-1199665544"])
telefonnummern.append(["Mike", "0178-8117428924"])  
telefonnummern.append(["Ama", "0159-28427222222"])

# Telefonnummer-Dictionary -> key:value --> O(1)
telefon_dict = {}
telefon_dict["Joey"] = "0151-1199665544"
telefon_dict["Mike"] = "0178-8117428924"
telefon_dict["Ama"] = "0159-28427222222"

# Wo steht der Name in der Liste? Unter welchen Index?
# Antwort für Ama: telefonnummern[2][0] -> y Wert ist Zeile, x=0 ist Name, x=1 ist Telefonnumer
name = input("Bitte gib die Telefonnummer für Name aus: ")
print(telefon_dict[name])

'''
for element in telefonnummern:
    if element[0] == name:
        print(element[1])
'''
