"""

    创建二级子进程处理僵尸(适合少量)

"""
import os
import time


def f1():
    for i in range(4):
        time.sleep(2)
        print("干嘛呢....")


def f2():
    for i in range(5):
        time.sleep(1)
        print("玩屁呀....")


pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    pid01 = os.fork()  # 二级子进程
    if pid01 == 0:
        f2()  # 二级子进程执行
    else:
        os._exit(0)
else:
    os.wait()
    f1()
