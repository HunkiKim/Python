A = int(input())
star = '*'
space = ' '
L = list()
for x in range(A):
    L.append(space)

for x in range(A):
    L[-(x+1)] = star
    print(''.join(L))
