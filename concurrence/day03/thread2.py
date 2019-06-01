"""

        线程编程(Thread)
示例
"""
from threading import Thread
import time
import os


# 线程函数
def fun(sec, name):
    print("线程函数传参")
    time.sleep(sec)
    print("%s 线程执行完毕" % name)

# 创建多个线程对象
jobs = []
for i in range(10):
    t = Thread(target=fun,args=(2.5,),kwargs={"name":"T%d"%i})

    jobs.append(t)
    t.start()

for i in jobs:
    i.join()