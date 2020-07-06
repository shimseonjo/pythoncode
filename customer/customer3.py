import customerF

def exe(choice):
    custlist=[{'name': '홍길동', 'gender': 'M', 'email': 'hong1@gmail.com', 'birthyear': 2000},
            {'name': '김길동', 'gender': 'M', 'email': 'kims1@gmail.com', 'birthyear': 2010},
            {'name': '박나리', 'gender': 'F', 'email': 'park1@gmail.com', 'birthyear': 1999},
            {'name': '김철수', 'gender': 'M', 'email': 'kim00@gmail.com', 'birthyear': 1988}]
    page=3
    
    if choice=='I':
        page = customerF.insertData(custlist,page)
    
    elif choice=='C':
        customerF.curSearch(custlist,page)
    
    elif choice=='P':
        page=customerF.preSearch(custlist,page)

    elif choice=='N':
        page=customerF.nextSearch(custlist,page)

    elif choice=='U':
        customerF.updateData(custlist)
    
    elif choice=='D':
        page=customerF.deleteData(custlist,page)
    
    elif choice=='Q':
        quit()


  
while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()  

    exe(choice)