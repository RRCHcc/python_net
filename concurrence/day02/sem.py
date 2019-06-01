"""

        信号量(信号灯集)

"""
from multiprocessing import Semaphore, Process
import time, os

# 创建信号量
# 服务程序最多允许三个进程同时执行事件
sem = Semaphore(3)


def handle():
    print("%d 想执行事件" % os.getpid())
    # 想执行事件，必须获取信号量
    sem.acquire()
    print("%d 开始执行操作" % os.getpid())
    time.sleep(3)
    print("%d 完成操作" % os.getpid())
    sem.release()  # 增加信号量


jobs = []
# 10 个进程请求执行事件
for i in range(6):
    p = Process(target=handle)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()

print(sem.get_value())  # 获取信号量值
