def f(A, x):
    res = (A % 25 == 0) and (x % 24 == 0 and (x % 75 == 0) <= (x % A == 0))
    return res


count = 0
for A in range(0, 10000 + 1, 25):
    for x in range(1, 10000 + 1):
        if not f(A, x):
            break
    else:
        count += 1

print(count)
