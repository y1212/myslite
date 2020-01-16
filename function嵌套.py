#三个数比较大小
# var01=int(input("word01: "))
# var02=int(input("word02: "))
# var03=int(input("word03: "))
#
# list01=[var01,var02,var03]
# maxNUM = list01[0]
# for element in list01:
#     if maxNUM <element:
#         maxNUM,element=element,maxNUM
# print(maxNUM)

#调用函数比较大小
def opera(*args):
    listA  =list(args)
    maxn =listA[0]
    for element in listA:
        if maxn <element:
            maxn,element=element,maxn
    return maxn
result =opera(200,625,53)
print(result)





#函数的嵌套
def Accumulate(number=0):
    if type(number) not in {str,int}:
        respose ='Please Check Your Input！'
        return respose    #当函数遇到return直到结束，不再继续运行

    def opera(number):
       result=0
       for n in range(number+1):
         result+=n
       return result
    return  opera(number)


result= Accumulate(5)
print(result)

