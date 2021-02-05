A = int(input())

for x in range(1, A):
    print(' ' * (A - x), end='')
    for y in range(1, x+1):
        print('*' + ' ', end='')
    print()

for x in range(1, A+1):
    print('*' + ' ', sep='', end='')
