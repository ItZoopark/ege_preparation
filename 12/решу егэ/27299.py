count = 61
while True:
    s = '1' * count
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '11', 1)

    if s == '221':
        print(count)
        break

    count += 1
