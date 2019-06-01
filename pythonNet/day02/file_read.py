"""
文件读操作演示
"""
import time

#打开文件返回文件对象
fd = open("text","r")

#读操作
#文件过大是不建议直接读到文件末尾
# while True:
#     time.sleep(1)
#     data = fd.read(2)
#     #如果读到空文件已经读完
#     if not data:
#         print("end")
#         break
#     print("读取到的内容:",data)
# while True:
#     time.sleep(2)
#     data = fd.readline()
#     if not data:
#         print("end")
#         break
#     print("RRRRR：",data)
#将读取内容作为列表返回
# data = fd.readlines(10)
# print("读取到的是：",data)
for line in fd:
    print("读取到：",line)
#关闭文件
fd.close()














