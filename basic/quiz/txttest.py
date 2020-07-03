f = open("./basic/quiz/test.txt",'w',encoding='utf-8')
f.write("txt파일 생성")
f.close()

f=open("./basic/quiz/test.txt","r",encoding="utf-8")
line ="a"
while line:
    line=f.readline()
    print(line)

f.close()