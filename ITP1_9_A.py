
w = input()
count = 0

while True:
    t = input()
    if t == 'END_OF_TEXT':
        break
    else:
        t = t.lower().split()
        for i in range(len(t)):
            if t[i] == w:
                count+=1

print(count)
