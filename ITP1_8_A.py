str = input()
list = list(str)

for i in range(len(list)):
    if list[i].isupper():
        list[i] = list[i].lower()
    else:
        list[i] = list[i].upper()

print("".join(list))
