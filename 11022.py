import string
n = int(input())
L = list()
CL = list()
DL = list()

for x in range(n):
    A = input()
    B = A.split(',')
    C = int(A[0])
    CL.append(int(A[0]))
    D = int(A[2])
    DL.append(int(A[2]))
    L.append(C + D)

num = 1

for x in L:
    s = "Case #"
    numb = str(num)
    new = s + numb + ": " + str(CL[num-1]) + " + " + str(DL[num-1]) + " = " + str(x)
    num += 1
    print(new)
