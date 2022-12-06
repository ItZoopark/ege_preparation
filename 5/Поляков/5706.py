N = 0
while True:
    N += 1
    N_bin = bin(N)[2:]
    if N_bin.count('1') % 2 == 0:
        N_bin = '10' + N_bin[2:] + '0'
    else:
        N_bin = '11' + N_bin[2:] + '1'

    R = int(N_bin, 2)
    if R > 40:
        print(N)
        break
