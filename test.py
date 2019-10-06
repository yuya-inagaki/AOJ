A, B, C = map(int, input().split())
coin = 0
date = 0
while coin < C:
    date += 1
    coin += A
    if date%7 == 0:
        coin += B
print(date)