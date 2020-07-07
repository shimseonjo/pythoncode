import re

class Customer:
    custlist=[{'name': '홍길동', 'gender': 'M', 'email': 'hong1@gmail.com', 'birthyear': 2000},
            {'name': '김길동', 'gender': 'M', 'email': 'kims1@gmail.com', 'birthyear': 2010},
            {'name': '박나리', 'gender': 'F', 'email': 'park1@gmail.com', 'birthyear': 1999},
            {'name': '김철수', 'gender': 'M', 'email': 'kim00@gmail.com', 'birthyear': 1988}]
    page=3

    def firstinput(self):
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
        return choice
    
    def exe(self,choice):
        if choice=='I':
            self.insertData()
            
        elif choice=='C':
            self.curSearch()
        
        elif choice=='P':
            self.preSearch()

        elif choice=='N':
            self.nextSearch()

        elif choice=='U':
            self.updateData()
        
        elif choice=='D':
            self.deleteData()
        
        elif choice=='Q':
            quit()



    def insertData(self): 
        print("고객 정보 입력")
        customer={'name':'','gender':'',"email":'',"birthyear":''}
        customer['name']=input("이름을 입력하세요 : ")
            
        while True:
            customer['gender']=str(input("성별(M/m 또는 F/f)을 입력하세요 : "))
            customer['gender']=customer['gender'].upper()
            if customer['gender'] in ('M','F'):
                break

        while True: # 중복되지 않게 입력
            customer['email']=str(input("이메일을 입력하세요 : "))
            check=0
            for i in self.custlist:
                if i['email']==customer['email']:
                    check=1

            p= re.compile('[a-z][a-z0-9]{4,}@[a-z]{2,}[.][a-z]{2,5}')
            result = p.match(customer['email'])
            
            if result != None and check==0:
                break
            elif result==None:
                print('"@"를 포함한 정확한 이메일을 써주세요') 
            elif check==1:
                print('중복되는 이메일이 있습니다.')     
        
        while True:
            customer['birthyear']=input("출생년도 4자리를 입력해주세요 : ")
            if len(customer['birthyear']) == 4 and customer['birthyear'].isdecimal() :
                customer['birthyear'] = int(customer['birthyear'])
                break

        self.custlist.append(customer)
        self.page += 1
        
    def curSearch(self):
        print("현재 고객 정보 조회")
        if self.page >= 0:
            print("현재 페이지는 {}쪽 입니다".format(self.page + 1)) 
            print(self.custlist[self.page])
        else:
            print("입력된 정보가 없습니다.")  

    def preSearch(self):
        if self.page <= 0:
            print('첫 번 째 페이지이므로 이전 페이지 이동이 불가합니다')
            print(self.custlist[self.page])
        else:
            self.page -= 1
            print("현재 페이지는 {}쪽 입니다".format(self.page + 1))
            print(self.custlist[self.page])

    def nextSearch(self):
        if self.page >= len(self.custlist)-1:
            print('마지막 페이지이므로 다음 페이지 이동이 불가합니다')
            print(self.custlist[self.page])
        else:
            self.page += 1
            print("현재 페이지는 {}쪽 입니다".format(self.page + 1))
            print(self.custlist[self.page])

    def deleteData(self):
        print("고객 정보 삭제")

        for i in self.custlist:
            print(i['name'],':',i['email'],end="  ")
        print()

        choice1 = input('삭제하려는 고객 정보의 이메일을 입력하세요.')
        delok = 0
        for i in range(0,len(self.custlist)):
            if self.custlist[i]['email'] == choice1:
                print('{} 고객님의 정보가 삭제되었습니다.'.format(self.custlist[i]['name']))
                del self.custlist[i]
                delok = 1
        
            if delok == 1:
                break

        if delok == 0:
                print('등록되지 않은 이메일입니다.')

        for i in self.custlist:
            print(i['name'],':',i['email'],end="  ")
        print()
        self.page = len(self.custlist)-1

    def updateData(self): 
        print("고객 정보 수정")
        while True:
            for i in self.custlist:
                print(i['name'],':',i['email'],end="  ")
            print()

            choice1=input('수정하시려는 고객 정보의 이메일을 입력하세요 : ') 
            idx=-1
            for i in range(0,len(self.custlist)):
                if self.custlist[i]['email'] == choice1:
                    idx=i
            if idx==-1:
                print('등록되지 않은 이메일입니다.')       
                break
                        
            choice2=input('''
    다음 중 수정하실 정보를 골라주세요 
        name, gender, birthyear
    (수정할 정보가 없으면 'exit' 입력)''')
            if choice2 in ('name','gender','birthyear'):
                self.custlist[idx][choice2]=input('수정할 {}을 입력하세요 :'.format(choice2))
                for i in self.custlist:
                    print(i['name'],':',i['email'],end="  ")
                print()
                break
            elif choice2 =='exit':
                break
            else:
                print('존재하지 않는 정보입니다.')
                break

    def __init__(self):
        while True:
            self.exe(self.firstinput())

Customer()
