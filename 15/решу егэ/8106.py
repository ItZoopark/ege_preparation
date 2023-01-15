for a in range(100, 0, -1):
    for x in range(1, 1000):
        if not (x % a != 0) <= ((x % 6 == 0) <= (x % 4 != 0)):
            break
    else:
        print(a)
        break