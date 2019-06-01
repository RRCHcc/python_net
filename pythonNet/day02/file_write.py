"""
文件写操作
"""

# fd = open("text","w")
fd = open("text", "a+")

fd.write("hello 玛利亚\n")
fd.write("hello 歌莉娅\n")
fd.write("hello 西莉亚\n")
fd.write("一起来玩啊\n")
#写入一个列表内容
fd.writelines(["hello\n","world\n"])

data = fd.read(10)
print(data)


#关闭文件
fd.close()
