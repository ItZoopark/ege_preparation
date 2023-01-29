f = open("27689.txt")
s = f.readline()

x_str = 'XYZ'
while True:
    if x_str + 'XYZ' in s:
        x_str += 'XYZ'
    else:
        if x_str + 'XY' in s:
            x_str += 'XY'
        else:
            if x_str + 'X' in s:
                x_str += 'X'
            else:
                break

print(len(x_str))


# x_str = 'XYZ'
# isX = True
# isY = False
# isZ = False
# while True:
#     if x_str in s:
#         if isX:
#             x_str += 'X'
#             isX = False
#             isY = True
#             isZ = True
#         elif isY:
#             x_str += 'Y'
#             isX = False
#             isY = False
#             isZ = True
#         elif isZ:
#             x_str += 'Z'
#             isX = True
#             isY = False
#             isZ = False
#     else:
#         print(len(x_str)-1)
#         break