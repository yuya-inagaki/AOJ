while True:
    table = input().split()

    a = int(table[0])
    b = int(table[2])
    op = table[1]
    if op == '?':
        break
    if op == '+':
        print(a+b)
    elif op == '-':
        print(a-b)
    elif op == '*':
        print(a*b)
    elif op == '/':
        print(int(a/b))
