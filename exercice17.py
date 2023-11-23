def exercice17():
    liste = [17, 38, 10, 25, 72]

    print(liste)
    for l in liste:
        print(l, end="\t")

    print()
    #liste.reverse ne retourne rien {none}
    liste.reverse()
    print(liste)
    for l in liste:
        print(l, end="\t")

    print()
    print(liste.index(17))

    liste.remove(38)
    print(liste)

    print(liste[1:3])

    print(liste[:2])

    print(liste[2:])

    print(liste[:])

    print(liste[-1])


exercice17()