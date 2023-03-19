import sys

f = open("5936.txt")
s = f.readlines()[0]

comb1 = 'XY'
comb2 = 'YZ'
comb3 = 'YZZ'

# s = 'ZZXZXZZXYYZYZZYYY'
curCount = 0
maxCount = 0

i = 0
l = len(s)
while i < l:
    if s[i:i + 2] == comb1:
        curCount += 2
        i += 2
    elif s[i:i + 3] == comb3:
        curCount += 3
        i += 3
    elif s[i:i + 2] == comb2:
        curCount += 2
        i += 2
    else:
        i += 1
        maxCount = max(maxCount, curCount)
        curCount = 0

print(maxCount)
