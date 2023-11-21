def exception_boucle():
    import math
    for n in range(-3, 4):
        print("pour x = ", n)
        try:
            print(" sin(", n, ")/", n, " = ", math.sin(n) / n)
        except ZeroDivisionError:
            print("Une division par 0 n'est pas possible")
        print("################")


if __name__ == '__main__':
    exception_boucle()
