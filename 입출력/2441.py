A = int(input())
star = '*'
space = ' '
L = list()
for x in range(A):
    L.append(star)

for x in range(A):
    print(''.join(L))
    L[x] = space