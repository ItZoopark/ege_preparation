from functools import reduce


def evens(x):  # x = 123
    l = []
    for d in str(x):
        if int(d) % 2 == 0:
            l.append(int(d))
    return l


def evens2(x):
    return list(map(int, filter(lambda c: int(c) % 2 == 0, str(x))))


def multiplyFlatten(l):
    evensList = [item for sublist in l for item in sublist]
    if len(evensList) != 0:
        return reduce(lambda x, y: x * y, evensList)
    else:
        return -1


def meetMask(x):
    xstr = str(x)
    if len(xstr) >= 3:
        if xstr[:2] == '11':
            if '6' in xstr:
                return True
    return False


# print(multiplyFlatten([evens(123), evens(456)]))

f = open("17-346.txt")
s = [int(x.strip()) for x in f]
count = 0
maxSum = 0
for i in range(len(s) - 2):
    res = multiplyFlatten([evens(s[i]), evens(s[i + 1]), evens(s[i + 2])])
    if res != -1 and res < 2 * 10 ** 9 and meetMask(res):
        count += 1
        maxSum = max(maxSum, res)
print(count, maxSum)
