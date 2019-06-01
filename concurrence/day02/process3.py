"""

    multiprocessing 模块创建进程

"""
from multiprocessing import Process
from time import sleep


# 带参数的进程函数
def worker(sec, name):
    for i in range(10):
        sleep(sec)
        print("I'm %s" % name)
        print("I'm working...")


# p = Process(target=worker, args=(2, "Baron"))
p = Process(target=worker,kwargs={"name":"Abby","sec":1})
p.start()
p.join()
