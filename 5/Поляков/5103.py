# a = set()
# for x in range(800, 1500 + 1):
#     R = bin(x)[2:]
#     if R[0] == '1' and R[1] == '1' and R[-2:] == '10':
#         N = int(R[1:-2], 2)
#         if N % 2 == 0:
#             a.add(N)
#     elif R[:2] == '11' and R[2] == '1' and R[-1] == '0':
#         N = int(R[2:-1], 2)
#         if N % 2 == 1:
#             a.add(N)
#
# print(a)

a = set()
for N in range(0, 1000000 + 1):
    if N % 2 == 0:
        N_bin = bin(N)[2:]
        R = int('1' + N_bin + '10', 2)
        if N_bin[0] == '1' and 800 <= R <= 1500:
            a.add(N)
    else:
        N_bin = bin(N)[2:]
        R = int('11' + N_bin + '0', 2)
        if N_bin[0] == '1' and 800 <= R <= 1500:
            a.add(N)

print(a)
