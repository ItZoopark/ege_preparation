def commonDigit(x, y):
    a = [int(el) for el in str(x)]
    b = [int(el) for el in str(y)]
    # if len(list(set(a).intersection(b))) != 0:
    #     return True
    # else:
    #     return False
    # l = min(len(a), len(b))
    l = len(a)
    count = 0
    for i in range(l):
        if a[i] == b[i]:
            count += 1

    if count == 1:
        return True
    else:
        return False


f = open("5206.txt")
s = [int(x.strip()) for x in f]
sum_max = sum(sorted(s)[-2:])
min_sum = float('inf')
count = 0
for i in range(len(s) - 2): # 0...len(s)-3
    if (commonDigit(s[i], s[i + 1]) or commonDigit(s[i], s[i + 2]) or commonDigit(s[i + 2], s[i + 1])) \
            and (s[i] + s[i + 1] + s[i + 2]) < sum_max:
        count += 1
        min_sum = min(min_sum, s[i] + s[i + 1] + s[i + 2])
print(count, min_sum)

