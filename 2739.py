A = int(input())
B = 1
if A >= 1 and A <= 9:
    for x in range(1,10):
        C = A * B
        print(str(A) + ' * ' + str(B) + ' = ' + str(C))
        B += 1