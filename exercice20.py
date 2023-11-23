def partie1():
    ch1 = "abc"
    ch2 = "de"
    liste = []

    for i in ch1:
        for j in ch2:
            liste.append(i+j)
    print(liste)


partie1()

def partie2():
    liste = list(range(6))
    print(liste)

    for i in liste:
        if i >= 2 :
            liste[i] = liste[i] + 3

    print(liste)

partie2()
