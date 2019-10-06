n, m, l = map(int, input().split())

A = list()
B = list()
C = [[0]*l for i in range(n)]

for i in range(n):
    A.append(list(map(int, input().split())))

for i in range(m):
    B.append(list(map(int, input().split())))

for i in range(n):
    for j in range(l):
        for k in range(m):
            C[i][j] += A[i][k]*B[k][j]

# for i in range(n):
#     for j in range(l):
#         print("%d"%C[i][j],end=" ")
#     print("")

for line in C:
    print(*line)
