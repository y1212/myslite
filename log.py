with open("story/access.log", "r", encoding="utf8") as log:
    ips={}
    while True:
        lines =log.readline()
        if not lines:
            break
        if lines.split()[6] in ips.keys():
            ips[lines.split()[6]]+=1
        else:
            ips[lines.split()[6]]=1
    print(ips)
    ip_sort = []
    for item in ips.items():
        ip_sort.append(item)
    for i in range(len(ip_sort)):
        for j in range(len(ip_sort) -1):
            if ip_sort[j][1] < ip_sort[j+1][1]:
                ip_sort[j],ip_sort[j+1]=ip_sort[j+1],ip_sort[j]
    print(ip_sort[:3])




    # ips={}
    # for lines in log.readlines():
    #     if lines.split()[0] in ips.keys():
    #         ips[lines.split()[0]] += 1
    #     else:
    #         ips[lines.split()[0]] =1
    # print(ips,type(ips))
    # ip_sort=[]
    # for item in ips.items():
    #     ip_sort.append(item)
    # for i in range(len(ip_sort)):
    #     for j in range(len(ip_sort) -1):
    #         if ip_sort[j][1] < ip_sort[j+1][1]:
    #             ip_sort[j],ip_sort[j+1]=ip_sort[j+1],ip_sort[j]
    # print(ip_sort[:3])



