grades = ['A','B','C','D','F']

while True:

    m, f, r = map(int, input().split())

    if m == -1 and f == -1 and r == -1:
        break

    if m ==-1 or f ==-1:
        print(grades[4])
    elif m + f >= 80:
        print(grades[0])
    elif m + f >= 65:
        print(grades[1])
    elif m + f >= 50:
        print(grades[2])
    elif m + f >= 30:
        if r >= 50:
            print(grades[2])
        else:
            print(grades[3])
    else:
        print(grades[4])
