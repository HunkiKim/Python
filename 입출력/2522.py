A = int(input())

for x in range(1 , A+1):
    print(' '*(A-x) + '*'*x)

for x in range(1 , A):
    print(' '*x + '*'*(A-x))