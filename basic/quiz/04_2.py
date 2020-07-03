import random,time

count=0
oper=['+','-','*','//']
input("게임시작(enter)")
start = time.time()
for x in range(0,3):
    a=random.randint(1,50)
    b=random.randint(1,50)
    op=random.choice(oper)
    quiz=str(a)+op+str(b)
    print(quiz,'=')
    print(eval(quiz))
    c=int(input('정답='))
    
    if int(eval(quiz))==c:
        print("정답!")
        count+=1
    else:
        print("오답!")

end = time.time()
print("차이 :", int(abs((end-start) - 20)), "초")
print("%d개 맞음"%count)