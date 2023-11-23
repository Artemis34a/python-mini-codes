def table(base, debut, fin, inc):
    for i in range(debut, fin + 1, inc):
        print(base, 'x', i, '=', base * i)

table(5,2,15,1)
