f = open("17.txt")
s = [int(x.strip()) for x in f]
n = 0
maxs = -1
l = len(s)
# print(*range(l))
# alt + shift + l - автовыравнивание
for i in range(l):
    for j in range(i + 1, l):
        if (s[i] - s[j]) % 60 == 0 and (s[i] % 15 == 0 or s[j] % 15 == 0):
            n += 1
            maxs = max(maxs, abs(s[i] - s[j]))

print(n, maxs)
