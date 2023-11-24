def partie1():
    print([t + p for t in list("abc") for p in list("de")])


partie1()

def partie2():
    print([t + 3 for t in list(range(6)) if t >= 2 ])


partie2()
