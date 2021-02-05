A = int(input())
B = input()

C = 0
if len(B) > A:
    print('error')
    exit()
else:
    for x in range(A):
        C += int(B[x])

print(C)


