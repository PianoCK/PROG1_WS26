# Bendford'sche Gesetz

zahlen = "0987234576345685498234509823473212345676873456750987456765434509834565434987584935654"
# Index    0  1  2  3  4  5  6  7  8  9  
zaehler = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for ziffer in zahlen:
    zaehler[int(ziffer)] += 1  

for ziffer in range(10):
    print(f"Die Zahl {ziffer} kommt {zaehler[ziffer]}x vor.")