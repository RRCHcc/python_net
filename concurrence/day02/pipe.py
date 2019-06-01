"""

        管道通信
注意点：
        如果父进程中大爱文件，创建进程通信对象或者创建套接字，
        子进程从父进程内存空间获取这些内容，那么父子进程对该对
        象的操作会有一定的属性关联

"""
from multiprocessing import Pipe
from multiprocessing import Process
import os, time

# 创建管道
fd1, fd2 = Pipe(False)


def fun(name):
    time.sleep(3)
    # 向管道写入内容
    fd2.send({name: os.getpid(), })


jobs = []
for i in range(5):
    p = Process(target=fun, args=(i + 1,))
    jobs.append(p)
    p.start()

for i in range(5):
    # 读取管道
    data = fd1.recv()
    print(data)

for i in jobs:
    i.join()
