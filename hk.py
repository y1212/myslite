#setence="ls , aa, cnm, sb"
# var=input("please input:")
# if var in setence:
#     setence=setence.replace("cnm","*")
#     print(setence)
#
# tuple=(1,2,3)
# list1=list(tuple[1])
# print(list1,type(list1))
# c,s =" ", "this is my house"
# d=s.split()
# d.reverse()
# for e in d:
#     c=c+e+" "
# print(c.lstrip())
# listB, listC = [], ["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]
# for element in listC:
#     if type(element) not in (int, float, str, bool):
#         for e in element:
#             listB.append(e)
#     else:
#         listB.append(element)
# print(listB)
# files= open(file="story/tt.txt",encoding="utf8")
# content=files.read()
# print(content)
# files.close()
#1、除二余一，a/3==2,a/4==3,a/5==4,a/6==5,a/7==9
a=7
while True:
    if a % 2 ==1 and a % 3 == 2 and a % 4 == 3 and a % 5 == 4 and a % 6 == 5 and a % 7 == 0:
        print(a)
        break
    else:
        a += 7
# 2. 使用while循环, 反转句子"hello Tony, this my sister"; 反转后为"sister my this, Tony hello";
s = 'hello Tony,this my sister'
list1 = s.split(',')
list_target = []
i = len(list1) - 1
while i >= 0:
    list0 = list1[i].split(' ')
    a = ' '.join(list0[::-1])
    list_target.append(a)
    i -= 1
str_target = ','.join(list_target)
print(str_target)

# A,B=[],"hello Tony, this my sister"
# list1=B.split(',')
# while len(list1)-1>=0:
#        list0=list1[len(list1)-1].split()
#        list1[]







# 3. 列表["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]转换成["string", "tuple", "list", 1, 2, 3, 4, 5, 6, 7];


listB, listC = [], ["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]
for element in listC:
    if type(element) not in (int, float, str, bool):
        for e in element:
            listB.append(e)
    else:
        listB.append(element)
print(listB)


4.#对[23, 12, 15, 11, 29, 24, 57, 21, 80, 99, 45]进行排序; 方式一: 要求使用for循环; 方式二: sorted函数;


listA = [23, 12, 15, 11, 29, 24, 57, 21, 80, 99, 45]
s=sorted(listA)
print(s)


# for循环
for i in range(len(listA)):
    for j in range(len(listA)):
        if listA[i]<listA[j]:
            listA[i],listA[j]=listA[j],listA[i]
    print(listA)


# 5. 元组("string", "world", 1, 2, 3, 4, 6, 9, 10), 把其中的数字提取到一个列表中;


listA, tupleA = [], ("string", "world", 1, 2, 3, 4, 6, 9, 10)
for element in tupleA:
    if type(element) in (int, float):
        listA.append(element)
print(listA,type(listA))


# 6. 提取access_log日志中所有的IP地址到字典ips中, 并根据ips中每个IP出现次数进行排序;


with open("story/access.log","r",encoding="utf8") as log:
    ips = {}
    while True:
        lines = log.readline()
        if not lines:
            break
        if lines.split()[0] in ips.keys():
            ips[lines.split()[0]] += 1
        else:
            ips[lines.split()[0]] = 1
    print(ips)
    ip_sort = []
    for item in ips.items():
        ip_sort.append(item)
    for i in range(len(ip_sort)):
        for j in range(len(ip_sort) - 1):
            if ip_sort[j][1] < ip_sort[j + 1][1]:
                ip_sort[j], ip_sort[j + 1] = ip_sort[j + 1], ip_sort[j]
    print(sorted(ip_sort))#正序
    print(ip_sort)#倒序

#7. 字符串"hello7723worl45d78", 把其中的数字提取到一个元组中;
str1 = "hello7723worl45d78"
str2 = "0123456789"
c = " "
for i in str1:
     if i in str2:
         c= c + i
print(tuple(c))






