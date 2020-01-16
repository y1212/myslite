#函数的调用
def add():
    a,b=12,13
    print(a+b)
add()
#用过的函数
# type()
# print()    len()
# open()   int()
# float()    str()
# bool()    list()
# tuple()    dict()
# set()

#函数的参数
def adds(a,b):
    print(a+b)
adds(a=12,b=2)
#调用的函数
# adds(a=13,b=34)
# for i in range(1,40):
#     adds(a=12,b=i)
# add(12,13)

adds(12,b=13)
# open("function.py","r", encoding="utf8")
# adds(12)

#函数的参数之默认参数
def addss(a=0,b=0):
    print("a is:{}".format(a))
    print("b is: {}".format(b))
    print("a + b = {}".format(a + b))
addss()

#只传a
addss(a=12)
addss(12)
#只传b
addss(b=13)

#print的功能实现
print(1,22,"word")

def printf(*args):
    print(args,type(args))
    if type(args[2])==str:
        print("hello {}".format(args[2]))
    else:
        print("args[2]'s type is not str")


printf(1,22,"word")

def printf(**kwargs):
    """:arg: ckovnrovnwr"""
    print(kwargs,type(kwargs))
    for items in kwargs.items():
        if items[0] == "sex":
            print(items[1])
printf(name='tom',age='18',sex='MAN')
#help(printf)
#不限制参数的长度也不限制参数的类型
def example(*args,**kwargs):
    pass

#函数的返回值
def add(a,b):
    return a+b
resault =add(12,13)
print(resault)


