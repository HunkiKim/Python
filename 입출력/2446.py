A = int(input())

for x in range(1 , A+1):
    print(' '*(x-1) + '*'*(A-x) + '*' + '*'*(A-x))

for x in range(1 , A):
    print(' '*(A-(x+1)) + '*'*x + '*' + '*'*x)


