# 함수 functions
# 입력값 parameters, 반환값 returns

def hello_friends(name):
    print("Habari, {}".format(name))

name_1 = "marco"
name_2 = "jane"
name_3 = "john"
name_4 = "tom"
name_5 = "tom"
name_6 = "tom"
name_7 = "tom"
name_8 = "tom"

# print("hi, {}".format(name_1))
# print("hi, {}".format(name_2))
# print("hi, {}".format(name_3))
# print("hi, {}".format(name_4))
# print("hi, {}".format(name_5))
# print("hi, {}".format(name_6))
# print("hi, {}".format(name_7))
# print("hi, {}".format(name_8))

hello_friends(name_1)
hello_friends(name_2)
hello_friends(name_3)
hello_friends(name_4)
hello_friends(name_5)
hello_friends(name_6)
hello_friends(name_7)
hello_friends(name_8)

# 입력값 유, 반환값 유
def sum(a,b):
    return a+b
# 입력값 유, 반환값 무
def hello_friends(name):
    print("hello, {}".format(name))
# 입력값 무, 반환값 유
def return_1():
    return 1
# 입력값 무, 반환값 무
def hello_world():
    print("hello world")
