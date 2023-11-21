def saisie_filtree() :
    while True :
        num = int(input("Entrez un nombre : "))

        if 1 > num or num > 10:
            print("Le nombre n'appartient pas à l'intervalle. ")
            break
        else :
            print("numero = ", num)


if __name__ == '__main__' :
    saisie_filtree()