def ordre_lexicographique():
    m1 = input("Entrez le premier mot :")
    m2 = input("Entrez le second mot :")
    if m1 == m2:
        print("Les deux mots sont identiques ")
    elif m1 < m2:
        print("Le mot ", m1, "vient avant le mot ", m2)
    else:
        print("Le mot ", m2, "vient avant le mot ", m1)


if __name__ == '__main__':
    ordre_lexicographique()