while True:
    h, w = map(int, input().split())
    if h==0 and w==0:
        break
    for i in range(h):
        for j in range(w):
            print('#', end="")
        print('')
    print('')
