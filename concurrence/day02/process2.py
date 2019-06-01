"""

    multiprocessing 模块创建进程

"""

from multiprocessing import Process
import time
import os


def th1():
    time.sleep(3)
    print("吃饭")
    print(os.getppid(), "--------", os.getpid())


def th2():
    time.sleep(2)
    print("睡觉")
    print(os.getppid(), "--------", os.getpid())


def th3():
    time.sleep(4)
    print("打豆豆")
    print(os.getppid(), "--------", os.getpid())


things = [th1, th2, th3]
jobs = []
for i in things:
    p = Process(target=i)
    jobs.append(p)  # 用列表保存进程对象
    p.start()
for i in jobs:
    i.join()
