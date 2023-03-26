def countDels(x):
    count = 0
    for d in range(1, int(x ** 0.5) + 1):
        if x % d == 0:
            if d != x // d:
                count += 2
            else:
                count += 1
    return count


maxCount = 0
minX = float('inf')
for x in range(84052, 84130 + 1):
    curCount = countDels(x)
    if curCount >= maxCount:
        maxCount = curCount
        minX = x
print(maxCount, minX)

# 2^4 = [2, 4, 8]
# 3^4 = [3, 9, 27]
# 3^4*2 = []
# 5^4 = [5, 25, 125]
# 2^4*3 = 48 = [2, 3, 4, 6, 8, 12, 16, 24]
