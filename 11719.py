# 최대 100줄 빈줄금지 공백끝금지
# 소문자 대문자 공백 숫자만
L = list()
num = 0
while 1:
    try:
        A = input()
        if len(A) > 100:
            print('error')
            exit()
        elif num == 100:
            break
        else:
            num += 1
            L.append(A)
    except EOFError:
        break
for x in L:
    print(x)




