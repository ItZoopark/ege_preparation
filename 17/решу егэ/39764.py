f = open("39764.txt")
s = [int(x.strip()) for x in f]
count = 0
maxSum = 0
for i in range(len(s) - 2):
    l = sorted([s[i], s[i+1], s[i+2]])
    if l[0]**2 + l[1]**2 == l[2]**2:
        maxSum = max(maxSum, sum(l))
print(count, maxSum)
