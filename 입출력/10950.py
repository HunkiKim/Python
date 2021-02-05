n = int(input())
C = []
for x in range(n):
    # 두 정수 A와 B를 입력받은 다음 A + B를 출력하는 프로그램을 작성하시오
    # 첫 줄에 A와 B가 주어진다 (0<A , B < 10)
    a = input()
    a.split(' ')
    if len(a) < 4:
        A = int(a[0])
        B = int(a[2])
        if A > 0 and B < 10:
            C.insert(x, A + B)
    else:
        print('error')

for x in C:
    print(x)
#test
