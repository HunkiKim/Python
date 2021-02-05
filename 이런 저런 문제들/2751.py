A = int(input())

num = list()
for x in range(0, A):
    num.append(int(input()))


num.sort()
for x in num:
    print(x)