#숫자를 입력받아서 짝수인지 홀수인지 판별

no = input("숫자를 입력하세요")
if no.isdecimal():
    no=int(no)
    if no%2 == 0:
        print("짝수")
    else:
        print("홀수")
else:
    print("숫자형이 아닙니다.")