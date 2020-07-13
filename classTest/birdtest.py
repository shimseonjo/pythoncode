# class Bird:
#     def fly(self):
#         raise NotImplementedError

# b = Bird()   
# b.fly() 

# class B(Bird):
#     def fly(self):
#         print("bird ")

# b1= B()
# b1.fly()

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명"
    

def say_nick(nick):
    if nick == '바보':
        raise MyError()


try:
    4/0
    say_nick("바보")
except MyError as err:
    print(err)
except Exception as err:
    print(err)