"""
二进制文件读操作
"""
#以二进制方式打开
fd = open("text","rb")

data = fd.read()
print(data.decode())

fd.close()