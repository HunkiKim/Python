
L = list()
while 1:
    A = input()
    B = A.split(' ')
    C = int(A[0])
    D = int(A[2])
    if C == 0 and D == 0:
        break
    else:
        L.append(C+D)

for x in L:
    print(x)
