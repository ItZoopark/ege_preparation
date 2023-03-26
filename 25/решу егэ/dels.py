def countDels(x):
    dels = []
    for d in range(1, int(x ** 0.5) + 1):
        if x % d == 0:
            if d != x // d:
                dels.append(d)
                dels.append(x // d)
            else:
                dels.append(d)
    if len(list(filter(lambda x: x % 2 == 0, dels))) == 3:
        print(x)


for x in range(101_000_000, 102_000_000 + 1):
    countDels(x)
