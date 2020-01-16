def  adds(number):
    if number ==1:
        return  number
    return number * adds(number-1)
print(adds(10))


import random
# def makeCode(length=4):
#     str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
#     code = ""
#     i = 0
#     while i < length:
#         code += str[random.randint(0,len(str)-1)]
#         i += 1
#     return code
# c = makeCode()
# print("生成的随机验证码为：",c)

# listB=[0,1,2,3,4,5,6,7,8,9]
# listA=input("please input a number: ")
# def makecode(length=4):
#     if listA in



# from time import *
# start_time = time()
# i=0
# while i<60:
#     print(i)
#     i+=1
#
# end_time = time()
# run_time = end_time-start_time
# print ('该循环程序运行时间：',run_time)
for i in range(1000):
 print(i)
