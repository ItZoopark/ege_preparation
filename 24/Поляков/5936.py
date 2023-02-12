import sys

sys.setrecursionlimit(100000)

# f = open("5936.txt")
# s = f.readlines()[0]

comb1 = 'XY'
comb2 = 'YZ'
comb3 = 'YZZ'


def calc(str, i, l):
    if i > len(str):
        return l
    elif str[i:i + 2] == comb1:
        return calc(str, i + 2, l + 2)
    elif str[i:i + 3] == comb3:
        return calc(str, i + 3, l + 3)
    elif str[i:i + 2] == comb2:
        return calc(str, i + 2, l + 2)
    else:
        calc(str, i + 1, l)


s = 'ZZXZXZZXYYZYZZYYY'
print(calc(s, 0, 0))
