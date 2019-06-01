"""
文件操作示例
"""
#打开文件
try:
    fd = open("text","a")
except FileNotFoundError as e:
    print(e)
else:
    print("打开成功")

    #开始你的读写操作

    #关闭文件
    fd.close()