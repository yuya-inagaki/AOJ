S = int(input())

h = int(S / 3600)
m = int((S % 3600) / 60)
s = (S % 3600) % 60

print(f"{h}:{m}:{s}")
