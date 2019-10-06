l = input().split()

w = int(l[0])
h = int(l[1])
x = int(l[2])
y = int(l[3])
r = int(l[4])

if 0 <= x-r and x+r <= w and 0 <= y-r and y+r <= h:
    print("Yes")
else:
    print("No")
