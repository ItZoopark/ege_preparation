i = 0
while True:
    N = 2 * i + 1
    N_bin = bin(N)[2:]
    N_bin_reverse = N_bin.replace('1', '2')
    N_bin_reverse = N_bin_reverse.replace('0', '1')
    N_bin_reverse = N_bin_reverse.replace('2', '0')
    R = N + int(N_bin_reverse, 2)
    if R > 99:
        print(N)
        break
    i += 1
