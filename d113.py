# ips = {'192.168.161.10': 13, '39.100.110.135': 8, '1.1.1.1': 11, '8.8.8.8': 5}
# print(ips)
# ips['192.168.12.16']=78
# print(ips)
# ips.setdefault('192.168.55.126',45)
# print(ips)
# ips.update([('17.17.17.17', 56), ('90.90.90.90', 78), ('12.12.12.12', 89)])
# print(ips)
# listA = ['192.168.161.10', '189.167.156.145', '10.10.10.10']
# ipaddr = {}.fromkeys(listA)
# print(ipaddr)
# ipaddr.pop('192.168.161.10')
# print(ipaddr)
# ipaddr.popitem()
# print(ipaddr)
# ipaddr.clear()
# print(ipaddr)
set01={1,2,3,4}
set02={3,4,5,6}
set03=set01&set02
print(set03)
set04 = set01 | set03
print(set04)
if 3 in set04:
    print(True)
else:
    print(False)
set04.add("hello")
print(set04)
set04.update([7,9,8])
print(set04)
set04.remove(9)
print(set04)
listA=[1, 3, 2, 4, 1,3, 2, 4, 9, 15, 22, 15, 18, 19, 17, 22, 43]
print(set(listA))
set04.pop()
print(set04)


