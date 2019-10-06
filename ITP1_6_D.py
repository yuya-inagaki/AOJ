

n, m = map(int, input().split())

a = list()
b = list()

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(m):
    b.append(int(input()))

# print(a)
# print(b)

for i in range(n):
    sum = 0
    for j in range(m):
        sum += b[j]*a[i][j]
    print(sum)
