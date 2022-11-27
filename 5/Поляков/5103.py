a = []
for R in range(800, 1500 + 1):
    isAlreadyIn = False
    tmp = []
    R_bin = bin(R)[2:]
    if R_bin[0] == '1' and R_bin[1] == '1' and R_bin[-2:] == '10':
        N = int(R_bin[1:-2], 2)
        if N % 2 == 0:
            isAlreadyIn = True
            tmp = [str(R), N]
    if R_bin[:2] == '11' and R_bin[2] == '1' and R_bin[-1] == '0':
        N = int(R_bin[2:-1], 2)
        if N % 2 == 1:
            if isAlreadyIn:
                tmp.append(N)

    if isAlreadyIn:
        a.append(tmp)

print(a)
collisions = list(filter(lambda item: len(item) > 2, a))
print("совпадений:", 2*len(collisions))
print("разные:", len(a) - len(collisions))

# print(sorted(a))

# a = list()
# for N in range(0, 1000000 + 1):
#     if N % 2 == 0:
#         N_bin = bin(N)[2:]
#         R = int('1' + N_bin + '10', 2)
#         if N_bin[0] == '1' and 800 <= R <= 1500:
#             a.append(N)
#     else:
#         N_bin = bin(N)[2:]
#         R = int('11' + N_bin + '0', 2)
#         if N_bin[0] == '1' and 800 <= R <= 1500:
#             a.append(N)

# print(a)
# print(len(a))
# print(len(set(a)))
