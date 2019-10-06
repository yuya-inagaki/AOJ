letters = "abcdefghijklmnopqrstuvwxyz"

table = [0]*26

while True:
    try:
        line = input()

        for i in line:
            index = 0
            for j in letters:
                if i == j or i == j.upper():
                    table[index]+=1
                index+=1
    except:
        break

for i in range(len(letters)):
    print("%s : %d"%(letters[i],table[i]))
