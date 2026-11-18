PI = 3.1415
MEHRWERTSTEUERSATZ = 0.19

def mwst_von_netto(netto):
    print(MEHRWERTSTEUERSATZ)
    return netto * MEHRWERTSTEUERSATZ

print(mwst_von_netto(100))