def suite():
    m = int(input("Entrez la valeur de m : "))
    import math
    return math.fsum([f ** 5 for f in range(m + 1)])


print(suite())
