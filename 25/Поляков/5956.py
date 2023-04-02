def countDels(x):
    dels1 = []
    dels2 = []
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            if d != x // d:
                dels1.append(d)
                dels2.append(x // d)
            else:
                dels1.append(d)
    return dels1 + dels2


# a=120 b=4
def isNod1(a, b):
    while a * b != 0:
        if a > b:
            a = a % b
        elif b > a:
            b = b % a
    if a + b == 1:
        return True
    else:
        return False


def checkPairs(p):
    # i = 0, j -> 1..5
    # i = 1, j -> 2..5
    # i = 2, j -> 3..5
    for i in range(6):
        for j in range(i + 1, 6):
            tmp = isNod1(p[i], p[j])
            if not tmp:
                return False
    return True


d = 2023
n = 1
count = 1
while n * d <= 10 ** 9 and count <= 5:
    x = n * d
    dels = countDels(x)
    if len(dels) >= 6:
        if checkPairs(dels[:6]):
            print(x)
            count += 1
    n += 1

print("-------------------")
x = 10**9
count = 1
while x >= 0 and count <= 5:
    if x % d == 0:
        dels = countDels(x)
        if len(dels) >= 6:
            if checkPairs(dels[:6]):
                print(x)
                count += 1
    x -= 1