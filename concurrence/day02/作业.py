"""
1.
mulitiprocess创建两个进程，
同时复制一个文件的上下两半部分，
各自复制到一个新的文件里
2.
复习：类
3.
将知识点示例代码看一下

"""

from multiprocessing import Process
import os


num = os.path.getsize("text")
half = num // 2


def copy_up():
    f = open("text", "rb")
    fd = open("file_up", "wb")
    data = f.read(half)
    fd.write(data)
    f.close()
    fd.close()


def copy_down():
    f = open("text", "rb")
    fd = open("file_down", "wb")
    f.seek(half)
    data = f.read(half)
    fd.write(data)
    f.close()
    fd.close()


c1 = Process(target=copy_up)
c2 = Process(target=copy_down)

c1.start()
c2.start()

c1.join()
c2.join()
