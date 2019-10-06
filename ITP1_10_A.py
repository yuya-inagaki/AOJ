import math
x1, y1, x2, y2 = map(float,input().split())

x = x1-x2
y = y1-y2

print(math.sqrt(x**2+y**2))
