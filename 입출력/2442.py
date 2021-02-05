A = int(input())
star = '*'
space = ' '

for x in range(1, A+1):
    print(' '*(A-x) + '*' * (1 + (2*(x-1))))

