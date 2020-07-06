import random,time,pickle,json,os

w=["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]

with open('./basic/quiz/rank.json','rt') as f:
    rank = json.load(f)

def sortV(x):
    return x[1]

while True:
   print('''
   1.타자게임 
   2.문제불러오기  
   3.문제저장하기  
   4.문제 등록 수정 삭제  
   5.등수 
   6.종료하기 ''')
   menu = input("  메뉴를 선택하세요>>>")
   if menu=='1':
        n=1
        q=random.choice(w)
        input('시작!')
        start = time.time()
        while n<=5:
            print("{}번".format(n))
            print(q)
            x=input()
            if q ==x:
                print("통과!")
                n=n+1
                q=random.choice(w)
            else:
                print("오타! 다시도전!")  
        end= time.time()
        print('타자 시간 : {:.0f}초'.format(end-start))  
        name = input("사용자 이름을 입력하세요")
        rank[name]=float(end-start)
        print(rank)
   elif menu=='2':
        with open('./basic/quiz/word.json','rt') as f:
            w = json.load(f)
   elif menu=='3':
        with open('./basic/quiz/word.json','wt') as f:
            json.dump(w,f,indent=4)          
   elif menu=='4':
        menu=input('1.등록  2.수정  3.삭제')
        if menu=='1':
            print(w)
            quiz=input('문제입력')
            w.append(quiz) 
            print(w)
        elif menu=='2':
            print(w)
            quiz=input('어떤 문제를 수정하나요?')
            index=w.index(quiz)
            quiz=input("수정내용")
            w[index]=quiz
            print(w)
        elif menu=='3':
            print(w)
            quiz=input('문제입력')
            w.remove(quiz)
            print(w)
        else:
            print("메뉴를 잘못 선택하셨습니다.")

   elif menu=='5':
        #ranklist=sorted(rank.items(),key=sortV)
        ranklist=sorted(rank.items(),key=lambda x:x[1])
        num=1
        for k,v in ranklist:
            print("%d등 %s %f" %(num,k,v))
            num = num+1
   elif menu=='6': 
       break
   else:
        print("메뉴를 잘못 선택하셨습니다.")

with open('./basic/quiz/rank.json','wt') as f:
    json.dump(rank,f,indent=4)