# -*- coding: utf-8 -*-
import random
fordeling = {}

# åpner en fil fra filnavn og returnerer en liste med innholdet
# et element per linje
def lesFraFil(filnavn):
    with open(filnavn) as fil:
        navneliste = fil.read().splitlines()
    fil.close()
    return navneliste

# genererer et pseudorandom nummer mellom 1 og 18 og tilordner det til navnet
def tilfeldigNummer(navn):
    random.seed()
    while(True):
        indeks = random.randint(5,21)
        # sjekker om tallet er tilordnet fra før
        if indeks not in fordeling:
            fordeling[indeks] = i
            break

# åpner fordeling.txt og skriver over det som er der fra før
def skrivTilFil():
    fil = open("fordeling.txt", "w")
    for key, value in fordeling.items():
        fil.write("{} : {}\n".format(key, value))
    fil.close()


# programmet starter her
elever = lesFraFil("navn.txt")
for i in elever: tilfeldigNummer(i)
skrivTilFil()



