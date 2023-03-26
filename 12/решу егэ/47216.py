def isPrime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


n = 1
while True:
    s = '>' + 39 * '0' + n * '1' + 39 * '2'
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)

    # s = s.replace('>', '')
    sum_digits = sum([int(c) for c in s if c != '>'])
    if isPrime(sum_digits) and len(s) == 3:
        print(n)
        break
    n += 1
