while True:
    h, w = map(int, input().split())
    if h==0 and w==0:
        break
    for i in range(h):
        for j in range(w):
            if i!=0 and i!=h-1 and j!=0 and j!=w-1 :
                print('.', end="")
            else:
                print('#', end="")
        print('')
    print('')
