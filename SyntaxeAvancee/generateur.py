def compteur(compteur):
    for i in range(compteur, 0, -1):
        yield i

for a in compteur(3):
    print(a)
for a in compteur(3):
    print(a)