s = list(input())

for i in range(int(input())):
    cmd, a, b, *c = input().split()
    a = int(a); b = int(b)
    if cmd == "print":
        print(*s[a:b+1], sep='')
    elif cmd == "reverse":
        s[a:b+1] = reversed(s[a:b+1])
    else:
        s[a:b+1] = c[0]
