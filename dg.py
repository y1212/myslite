# 求十的阶乘
# def addr(number):
#     if number == 1:
#         return number
#     return number * addr(number-1)
# print(addr(10))
#求1-100的和
import  os
# sums =0
# for i in range(101):
#     sums += i
#     print(sums)
#
# def add(n=10):
#     if n ==0:
#         return n
#     return n +add(n-1)
# print(add(10))


dirC = fileC =0
def  getCount(path):
    for files in os.listdir(path):
        fileAbs=os.path.join(path,files)
        if os.path.isdir(fileAbs):
            global dirC
            dirC+=1
            getCount(fileAbs)
        else:
            global fileC
            fileC+=1
    return dirC,fileC
dirCount,fileCount=getCount("F:\PythonDemo")
print('dirCount:{},fileCount:{}'.format(dirC,fileC))



