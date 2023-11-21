def methode1():
    nom = input("Veulliez entrer votre nom : ")
    age = input("Veulliez entrer votre age : ")
    return print("Votre nom est ", nom, " et vous avez ", age, " ans")


def methode2():
    nom = input("Veulliez entrer votre nom : ")
    age = int(input("Veulliez entrer votre age : "))
    return print("Votre nom est ", nom, " et vous avez ", age, " ans")


if __name__ == '__main__':
    methode1()
    print("Passons à la seconde méthode ")
    methode2()
