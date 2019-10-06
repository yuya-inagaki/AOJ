r, c = map(int, input().split())

table = list()


for i in range(r):
    table.append(list(map(int, input().split())))
    table[i].append(sum(table[i]))

table.append([])
for j in range(c+1):
    sum = 0
    for i in range(r):
        sum += table[i][j]
    table[r].append(sum)

for i in range(r+1):
    print("%d"%table[i][0],end = "")
    for j in range(1, c+1):
        print(" %d"%table[i][j],end = "")
    print("")
