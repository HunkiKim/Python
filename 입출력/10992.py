A = int(input())

for x in range(1, A):
    if(x == 1):
        print(' ' * (A - x), end='')
        print('*' + ' '*x , end='')
        print()
    else:
        print(' ' * (A - x), end='')
        print('*' + ' ' * ((x-1)*2-1) + '*', end='')
        print()


print('*'*(A*2-1), sep='', end='')
