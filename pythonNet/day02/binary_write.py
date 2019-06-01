"""
二进制文件写操作
"""
#以二进制方式打开
fd = open("text","wb")

fd.write(b"hello world")#写入字节串


fd.close()