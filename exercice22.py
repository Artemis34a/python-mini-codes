def anneeBissextile(a):
    return a % 4 and not a % 100 or a % 400
    # a % 4 : this expression checks if a is divisible by 4.
    # not a % 100 : this expression checks if a is not divisible by 100.
    # a % 400 : this expression checks if a is divisible by 400


def verification():
    a = int(input("Veulliez entrez l'année "))
    if anneeBissextile(a):
        print("L'anné ", a, " est une année bissextile")
    else:
        print("L'année ", a, " n'est pas une année bissextile.")


verification()
