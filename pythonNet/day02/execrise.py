"""
练习：
在终端输入一个文件名称（可以夹带路径），
将该文件赋值到当前目录下，并且重名为xxxx
要求可以复制所有类型文件
"""

fine_name = input("myfilename：")
try:
    fd = open(fine_name,"rb")
except FileNotFoundError as e:
    print(e)
else:
    f = open("myfile","wb")
#循环输入文件内容写入到myfile文件
    while True:
        data = fd.read(1024)
        if not data:
            break
        f.write(data)
    fd.close()
    f.close()

