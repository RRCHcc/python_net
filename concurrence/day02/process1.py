"""

    multiprocessing 模块创建进程

"""
import multiprocessing as mp
import time

# 子进程函数
a = 1


def fun():
    print("子进程开始执行")
    global a
    print("a = ", a)
    a = 10000
    time.sleep(3)
    print("子进程执行完毕")


# 创建进程对象

p = mp.Process(target=fun)

# 启动进程
p.start()
time.sleep(2)
print("父进程")

# 回收进程
p.join()
print("a = ",a)