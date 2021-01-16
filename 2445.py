A = int(input())

for x in range(1 , A+1):
    print('*'*x + ' '*(A-x) + ' '*(A-x) + '*'*x)

for x in range(1 , A):
    print('*'*(A-x) + ' '*(x*2) + '*'*(A-x))