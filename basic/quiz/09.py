import random, time

w=["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]

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