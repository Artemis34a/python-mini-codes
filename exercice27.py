def diviseurs_de(a):

    b = [f for f in range(1, a+1) if not a % f]
    print("La liste des diviseurs de ", a ," sont : ", b)

diviseurs_de(9)
diviseurs_de(3)
diviseurs_de(200)