def boucle_a_b():
    a = 0
    b = 10

    while a < b:
        print("a = ", a)
        a += 1
    while b != 0 :
        b -= 1
        if b % 2 == 0 :
            print("b = ", b)


if __name__ == '__main__' :
    boucle_a_b()