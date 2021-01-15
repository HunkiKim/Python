import re
reg = re.compile(r'[a-zA-Z]')
A = input()
L = list()

if A == '':
    print('error')
    exit()
elif len(A) > 100:
    print('error')
    exit()
else:
    if reg.match(A):
        num = len(A) / 9 + 1
        s = 0
        num = int(num)
        for x in range(num):
            print(A[s:(x+1)*10]) # 0~10 0-9 10-20
            s = (x+1) * 10
    else:
        print('fucking')
