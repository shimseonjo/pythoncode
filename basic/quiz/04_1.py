import random

count=0
for x in range(0,3):
    a=random.randint(1,50)
    b=random.randint(1,50)
    print("%d + %d = "%(a,b))
    c=int(input())
    if a+b==c:
        print("정답!")
        count+=1
    else:
        print("오답!")
print("%d개 맞음"%count)