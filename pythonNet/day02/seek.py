"""
文件偏移量
"""

# fd = open("text","w+")
#
# fd.write("hello world")
# fd.flush()
# data = fd.read()#文件偏移量在哪从哪里开始读
# print(data)
# fd.close()

fd = open("text","r+")
#相对开头位置向后偏移了多少
print("当前文件偏移量：",fd.tell())#0
print(fd.read(2))
print("当前文件偏移量：",fd.tell())#2
print(fd.read(2))
fd.seek(5,0)
print(fd.read(2))
print("当前文件偏移量：",fd.tell())#2
fd.close()




