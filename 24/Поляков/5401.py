import re

# f = open("5401.txt")
# s = f.readlines()[0]
s = 'BDADBADBADBABDAFABDA'
# s = 'BCABCABCABF'
lst = s.split('A')
# print(max(lst, key=len))
# print(max(lst, key=len) in lst)
# print(lst)
maxCount = 0
curCount = 0
curLen = 0
count = 0
# print(lst)
# BDADBADBADBABDAFABDA
# ADBADBADBA
# ABDAABDA -> ['','BD','','BD','']
# ADBADBADBA -> ['DB', 'DB', 'DB', 'R']
for i in range(len(lst) - 2):
    if lst[i + 1] == lst[i + 2] != '':
        count += 1
        if count > 2:
            continue
        curCount += 1
        countA = 2 * curCount + curCount % 2
        between = (countA - 1) * len(lst[i])
        curLen = (countA + between)
    elif count == 2 and curLen != 0:
        maxCount = max(maxCount, curLen)
        curCount = 0
        count = 0
print(maxCount)
