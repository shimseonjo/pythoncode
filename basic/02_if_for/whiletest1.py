prompt = '''
------------------------
   커피 자판기 메뉴
------------------------
 1. 커피 메뉴 입력
 2. 커피 메뉴 삭제
 3. 커피 자판기
 4. 커피메뉴판
 5. 종료
-------------------------
 메뉴선택 >>>> '''
menudic = {'coffe':2000,'카페라떼':3500,'오렌지쥬스':4000}

while True:
    print(prompt)
    menu = input()
    print(menu)
    if menu == '1':
        print("커피메뉴를 추가합니다")
        name = input("메뉴명 >>> ")
        price = int(input("가격 >>> "))
        menudic[name]=price
        print(menudic)
        print(" {}메뉴는 {:,}원 입니다.".format(name,price))
    elif menu == '2':
        print("커피메뉴를 삭제합니다.")
        print(menudic)
        name = input("삭제할 커피메뉴 >>> ")
        menudic.pop(name)
        del menudic[name]
        print(menudic)
    elif menu == '3':
        print("커피자판기 시작!!")
        print(menudic)
        choicemenu = input("커피메뉴를 선택하세요 >>")
        inputmeney = int(input("금액을 입력하세요 >>"))
        # if choicemenu not in menudic:
        if menudic.get(choicemenu)== None:
            print("메뉴없음")
        else :
            if menudic[choicemenu]>inputmeney:
                print("금액이 부족합니다.")
            else:
                print("{} 음료가 나옵니다.".format(choicemenu))
                print("남은 금액 {}을 받으세요".format(inputmeney-menudic[choicemenu]))
    elif menu == '4':
        print('''
----------------------------
         M  E  N  U
----------------------------''')
        for k,v in menudic.items():
            print("{}    {:,}원 ".format(k,v))      
    elif menu == '5':
        print("프로그램 종료")
        break
