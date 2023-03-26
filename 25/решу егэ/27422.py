def countDels(x, count):
    dels = []
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            if d != x // d:
                dels.append(d)
                dels.append(x // d)
            else:
                dels.append(d)
    if len(dels) == count:
        print(dels)

def twoDels(x):
    dels = []
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            if d != x // d:
                dels.append(d)
                dels.append(x // d)
            else:
                dels.append(d)
            if len(dels) > 2:
                return []
    if len(dels) == 2:
        return dels
    else:
        return []


for x in range(174457, 174505 + 1):
    countDels(x, 2)