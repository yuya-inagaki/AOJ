while True:
    line = input()
    if line == '0':
        break
    print(sum(int(x) for x in line))
