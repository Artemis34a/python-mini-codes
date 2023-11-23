import math


def volMasseEllipsoide(a = 0, b = 0, c = 0, masse_vol = 0):

    return (4*(math.pi * a * b * c))/3, (4*(math.pi * a * b * c))/3 * masse_vol


print(volMasseEllipsoide(), volMasseEllipsoide(13, 2, 33, 15))