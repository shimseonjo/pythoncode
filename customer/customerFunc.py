import re

def insertData(page,custlist):        
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
        for i in custlist:
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

    custlist.append(customer)
    page += 1

    print(customer)
    print(custlist)
    print(page)
    return page
  
def curSearch(page,custlist):
    print("현재 고객 정보 조회")
    if page >= 0:
        print("현재 페이지는 {}쪽 입니다".format(page + 1)) 
        print(custlist[page])
    else:
        print("입력된 정보가 없습니다.")  


def preSearch(page,custlist):
    print("이전 고객 정보 조회")
    if page <= 0:
        print('첫 번 째 페이지이므로 이전 페이지 이동이 불가합니다')
        print(custlist[page])
    else:
        page -= 1
        print("현재 페이지는 {}쪽 입니다".format(page + 1))
        print(custlist[page])
    return page
        
def nextSearch(page,custlist):
    print("다음 고객 정보 조회")
    if page >= len(custlist)-1:
        print('마지막 페이지이므로 다음 페이지 이동이 불가합니다')
        print(custlist[page])
    else:
        page += 1
        print("현재 페이지는 {}쪽 입니다".format(page + 1))
        print(custlist[page])
    return page


def deleteData(custlist):
    print("고객 정보 삭제")

    for i in custlist:
        print(i['name'],':',i['email'],end="  ")
    print()

    choice1 = input('삭제하려는 고객 정보의 이메일을 입력하세요.')
    delok = 0
    for i in range(0,len(custlist)):
        if custlist[i]['email'] == choice1:
            print('{} 고객님의 정보가 삭제되었습니다.'.format(custlist[i]['name']))
            del custlist[i]
            delok = 1
    
        if delok == 1:
            break

    if delok == 0:
            print('등록되지 않은 이메일입니다.')

    for i in custlist:
        print(i['name'],':',i['email'],end="  ")
    print()
    page = len(custlist)-1
    return page

def updateData(custlist): 
    print("고객 정보 수정")
    while True:
        for i in custlist:
            print(i['name'],':',i['email'],end="  ")
        print()

        choice1=input('수정하시려는 고객 정보의 이메일을 입력하세요 : ') 
        idx=-1
        for i in range(0,len(custlist)):
            if custlist[i]['email'] == choice1:
                idx=i
        if idx==-1:
            print('등록되지 않은 이메일입니다.')       
            break
                    
        choice2=input('''
다음 중 수정하실 정보를 골라주세요 
    name, gender, birthyear
(수정할 정보가 없으면 'exit' 입력)''')
        if choice2 in ('name','gender','birthyear'):
            custlist[idx][choice2]=input('수정할 {}을 입력하세요 :'.format(choice2))
            for i in custlist:
                print(i['name'],':',i['email'],end="  ")
            print()
            break
        elif choice2 =='exit':
            break
        else:
            print('존재하지 않는 정보입니다.')
            break

