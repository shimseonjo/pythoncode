for x in range(2,10):
    print("\n--[%d단]--"%x)
    for y in range(1,10):
        print("%d x %d = %2d" %(x,y,x*y))

print()

for x in range(1,10):
    for y in range(2,10):
        #print("%d x %d = %2d" %(y,x,x*y),end='  ')
        print("{} x {} = {:2}".format(y,x,x*y),end='  ')
    print()


a = [1,2,3,4,5]
result = [num*3 for num in a if num % 2 ==0]
print(result)
result = []

for num in a:
    if num%2 == 0:
        result.append(num*3)

print(result)