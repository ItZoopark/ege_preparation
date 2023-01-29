f = open("27421.txt")
s = [x for x in f][0]
cur_count = 1
max_count = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cur_count += 1
    else:
        max_count = max(max_count, cur_count)
        cur_count = 1

print(max_count)
