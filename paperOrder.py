def kleinsteFläche(liste):
    liste = sorted(liste)
    return liste[0] * liste[1]

def kleinsterUmfang(liste):
    liste = sorted(liste)
    return 2 * (liste[0] + liste[1])
    
bandLänge = 0
gesamtFläche = 0
daten = open('wrappingPaper.txt','r')
for zeile in daten:
    paket = zeile.rstrip('\n')
    masse = paket.split('x')
    länge = int(masse[0])
    breite = int(masse[1])
    höhe = int(masse[2])
    oberfläche = 2 * (breite * länge + breite * höhe + länge * höhe)
    bestellFläche = oberfläche + kleinsteFläche([länge, breite, höhe])
    gesamtFläche += bestellFläche
    bandLänge += länge * höhe * breite + kleinsterUmfang([länge, breite, höhe])
daten.close()
print(gesamtFläche)
print(bandLänge)