def enceinte_pressurisée():
    pSeuil = 2.3
    vSeuil = 7.41

    pCourante = float(input("Veuillez rentrer la pression courante :"))
    vCourant = float(input("Veuillez entrer le volume courant :"))

    if pCourante > pSeuil and vCourant > vSeuil :
        print("Arret immediat de l'enceinte pressurisée. ")
    elif pCourante > pSeuil and vCourant < vSeuil :
        print(" Veuillez augmenter le volume de l'enceinte ")
    elif pCourante < pSeuil and vCourant > vSeuil :
        print(" Veuillez diminuer le volume de l'enceinte")
    else :
        print("Tout va bien.")


if __name__ == '__main__':
    enceinte_pressurisée()