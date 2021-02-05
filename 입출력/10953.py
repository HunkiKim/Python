n = int(input())
L = list()


for x in range(n):
    A = input()
    B = A.split(',')
    C = int(A[0])
    D = int(A[2])
    L.append(C + D)

for x in L:
    print(x)
