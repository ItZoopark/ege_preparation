N = 2
i = 1
while True:
    N = 2 * i + 1
    N_bin = bin(N)[2:]
    N_bin_inv = N_bin[0] + N_bin[1:].replace('1', '|')\
        .replace('0', '1')\
        .replace('|', '0')
    N_inv = int(N_bin_inv, 2)
    R = N + N_inv
    if R > 99:
        print(N)
        break
    i += 1

# orig = '101111001'
# tmp = orig[1:]
# print(orig)
# res = tmp.replace('1', '|')\
#     .replace('0', '1')\
#     .replace('|', '0')
# print('1' + res)