def fun(element):
    return element ** 3
list01=[1, 12, 56, 3]
n=map(fun,list01)
print(list(n))

def residual(element):
    if element % 2 == 0:
        return element

result=filter(residual,range(5))
print(list(result))
result=map(residual,range(10))
print(list(result))
print(result)



from functools import reduce
def nick(x, y):
    return x  + y


number = [1, 2, 3, 4, 5]
prod = reduce(nick, number)
print(prod)



from function import reduce
def adds(x,y):
    return x+y
addss=reduce(adds,range(101))
print(list(addss))


#匿名函数
def add(a=0,b=0):
    return a+b
qiuhe = lambda a,b:a+b
print(add(13,15))
print(qiuhe(13,25))

#sorted函数
ip={'192.168.161.10': 13, '39.100.110.135': 8, '1.1.1.1': 11, '8.8.8.8': 5}
ips=sorted(ip.items(),key=lambda x:x[1],reverse=True)#正常是false，所以不用填，输出的是正序
print(ips)