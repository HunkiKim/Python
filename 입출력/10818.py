A = int(input())
B = input()
Li = list()
L = B.split(' ')
for x in range(A):
    Li.append(int(L[x]))
mi = min(Li)
ma = max(Li)
print(str(mi) + ' ' + str(ma))

