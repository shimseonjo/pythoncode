

myList = [4, 2, 3, 5, 1]
myList.sort()
print(myList)

myDic = {1:1,3:3,2:2}
myDic.sort()
print(myDic)


#str
sorted("hello",reverse=True)                         

#list
sorted([5,2,1,3,4])                     
sorted([[2,1,3],[3,2,1],[1,2,3]])       

#set
sorted({3,2,1})                         

#tuple
sorted((3,2,1))                         

#dict
sorted({3:1,2:3,1:4})                   

#vlaue값을 기준으로 정렬? sorted함수의 파라미터인 key를 이용
#dict
myDict = {3:1,2:3,1:4}

# [(3, 1), (2, 3), (1, 4)]
sorted(myDict.items(),key=lambda x: x[1])

# 2번째 문자를 기준으로 정렬(각각 e, i, y)
sorted(['abc','bac', 'python'],key=lambda x:x[1],reverse=True)

# 내림차순으로 정렬하고 싶은경우에는 파라미터 reverse 값을 true로
sorted(range(1,10),reverse=True)
