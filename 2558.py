#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#두 정수 A와 B를 입력받은 다음 A + B를 출력하는 프로그램을 작성하시오
# 첫 줄에 A와 B가 주어진다 (0<A , B < 10)
a = input()
b = input()
A = int(a)
B = int(b)
if A > 0 and B < 10:
    C = A + B
    print(C)
else:
    print('error')
