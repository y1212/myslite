import os
os.listdir("story")
print(os.listdir("story"))
print(os.getcwd())
os.chdir("story")
print(os.getcwd())
if os.path.isdir("story"):
    print("story is directory")#isfile(查看是否为文件)
else:
    print("story not directory")

if os.path.exists("log.py"):
    print("exists")
else:
    print("not exists")



