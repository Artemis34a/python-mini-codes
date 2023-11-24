def anneeBissextile():
    a = int(input("Veulliez entrez l'année "))
    return print( a % 4 and a % 100 or a % 400)


anneeBissextile()