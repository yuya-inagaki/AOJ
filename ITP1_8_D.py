
s = input()
p = input()

s=s+s[:-1] #始点から最後から一つ前の文字まで取得して連結
if s.find(p)!=-1:
    print("Yes")
else:
    print("No")
