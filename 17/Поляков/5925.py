f = open("17-353.txt")
s = [int(x.strip()) for x in f]
count = 0
maxSum = 0
for i in range(len(s) // 2):
    l = i
    r = len(s) - 1 - i
    mean = (max(s) + min(s)) / 2
    if max(s[l], s[r]) > mean > min(s[l], s[r]):
        count += 1
        maxSum = max(maxSum, s[l] + s[r])
print(count, maxSum)
# 12
# 6
# 0..5 6..11
# 13
# 6
# 0..5 7..12