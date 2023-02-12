f = open("33196.txt")
s = f.readlines()[0]
list = list(filter(lambda x: len(x) != 0, s.split('A')))

# 'ABFDGABDFAC' -> ['BFDG', 'BDF', 'C']
# {'key1':'value1', 'key2':'value2'}
# {'A':0, 'B':0, ... 'Z':0}
# {'A':0, 'B':5, ... 'Z':3}
dict = {chr(code): 0 for code in range(ord('A'), ord('Z')+1)}

for item in list:
    dict[item[0]] += 1

print(sorted(dict.items(), key=lambda x: x[1], reverse=True)[0][0])
