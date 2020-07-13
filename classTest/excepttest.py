#FileNotFoundError
# f=open("./classTest/test.txt","r")

#ZeroDivisionError
# 4/0

#IndexError
# li=[2,3,4]
# li[3]

try:
    # 4/1
    4/0
    # f=open("./classTest/test.txt","r")
    # li=[2,3,4]
    # li[3]
except IndexError as err:
    print(err)
except ZeroDivisionError as err:
    pass
except FileNotFoundError as err:
    print(err)
finally:
    print('finally')