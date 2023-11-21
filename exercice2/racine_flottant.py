def racine_flottant():
    try :
        num = float(input("Entrez un nombre :"))
        import math
        print("La racine carré de ", num," est : ", math.sqrt(num))
    except ValueError:
        print(" Erreur sur le nombre entré.")


if __name__ == '__main__':
    racine_flottant()