def soustraction(a, b):
    return a+b

def addition(a, b):
    resultat = a + b
    resultat = soustraction(resultat, b)
    return resultat


liste1 = [5, 6]
liste2 = [3, 7]
addition(liste1, liste2)

print("end")
