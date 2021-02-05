A = input()

Day = A.split(' ')

M = int(Day[0])
D = int(Day[1])
num = D

for n in range(1 , M):
    if n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10:
        num += 31
        n += 1
    elif n == 4 or n == 6 or n == 9 or n == 11:
        num += 30
    else:
        num += 28


num %= 7
if num == 1:
    print('MON')
elif num == 2:
    print('TUE')
elif num == 3:
    print('WED')
elif num == 4:
    print('THU')
elif num == 5:
    print('FRI')
elif num == 6:
    print('SAT')
else:
    print('SUN')

