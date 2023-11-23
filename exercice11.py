def cube(num):
    return num**3


print(cube(3), cube(2), cube(1))


def volumesphere(rayon):
    import math
    return (4*math.pi*(cube(rayon)))/3


print(volumesphere(4), volumesphere(5))
