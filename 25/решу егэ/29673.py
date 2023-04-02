def isPrime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


l = 123456789
r = 223456789
start = int(l ** 0.25) + 1
while start ** 4 < r:
    if isPrime(start):
        print(start ** 4, start ** 3)
    start += 1

# 2^4 = 4^2 = 16 = [2, 4, 8]
# 3^4 =  9^2 = 81 = [3, 9, 27]
# 5^4 = 25^2 =  625 = [5, 25, 125]
# 7^4 = 2401 = [7, 49, 343]

# НОД(6,5) = 1
# Cnk = n!/(k!*(n-k)!)
# C62 = 6*5/ (2) = 15
# 1 2 3 4 5 6
# 1 -> 5
# 2 -> 4
# 3 -> 3
# 4 -> 2
# 5 -> 1

