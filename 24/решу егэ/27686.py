f = open("27421.txt")
s = f.readline()

x_str = 'X'
while True:
    if x_str in s:
        x_str += 'X'
    else:
        print(len(x_str) - 1)
        break
