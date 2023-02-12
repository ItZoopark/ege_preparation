f = open("33526.txt")
s = f.readlines()[0]

dict = {chr(code): 0 for code in range(ord('A'), ord('Z') + 1)}

for i in range(1, len(s) - 1):
    if s[i - 1] == s[i + 1]:
        dict[s[i]] += 1

print(sorted(dict.items(), key=lambda x: x[1], reverse=True)[0][0])
