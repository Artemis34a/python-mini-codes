def gestionTVA(valeur):
    ttc = (119.25 * valeur) / 19.25
    ht = (valeur * 100) / 19.25

    return ttc, ht


(a, b) = gestionTVA(111789.52)
print((a, b))
