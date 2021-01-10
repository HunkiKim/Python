import string
n = int(input())
L = list()


for x in range(n):
    A = input()
    B = A.split(',')
    C = int(A[0])
    D = int(A[2])
    L.append(C + D)

num = 1

for x in L:
    s = "Case #"
    s
    print('Case #'+ s + x)
    num += 1
