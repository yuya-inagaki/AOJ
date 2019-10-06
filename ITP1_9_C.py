# letters = "abcdefghijklmnopqrstuvwxyz"
#
# n = int(input())
#
# pt = 0
# ph = 0
#
# for i in range(n):
#     taro, hanako = input().split()
#
#     length_taro = len(taro)
#     length_hanako = len(hanako)
#
#     for j in range(length_taro):
#         flag = 0
#         for l in letters:
#             if taro[j] == l and hanako[j] == l:
#                 if j == length_taro-1:
#                     if length_taro < length_hanako:
#                         ph += 3
#                         break
#                     else:
#                         pt += 1
#                         ph += 1
#                         break
#                 else:
#                     break
#             elif taro[j] == l:
#                 ph += 3
#                 flag = 1
#                 break
#             elif hanako[j] == l:
#                 pt += 3
#                 flag =1
#                 break
#
#         if flag == 1:
#             break;
#
# print("%d %d"%(pt, ph))

h=t=0
for _ in range(int(input())):
    a,b=input().split()
    if a>b:
        t+=3
    elif a<b:
        h+=3
    else:
        t+=1
        h+=1
print(t,h)
