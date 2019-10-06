
room = [[[0]*10 for i in range (0,3)] for k in range (0,4)]

#print(room)

N = int(input())

for loop in range(N):

    b, f, r, v = map(int, input().split())

    room[b-1][f-1][r-1] += v

    #print(room)

for i in range(0,4):
    for j in range(0,3):
        for k in range(0,10):
            print(" %d"%room[i][j][k],end = "")
        print("")
    if i < 3:
        print("#"*20)
