
while True:
    C = input()
    if C == "-":
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        # print("%s %s"%(C[h:],C[:h]))
        C = C[h:] + C[:h] #h+1番目以降の+h番目まで(スライスを使用)
    print(C)
