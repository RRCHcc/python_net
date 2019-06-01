"""

        消息队列

"""
from multiprocessing import Queue
from multiprocessing import Process
import os, time
import random

# 创建消息队列对象
q = Queue(5)


def fun():
    for i in range(20):
        x = random.randint(0, 999)
        y = random.randint(0, 999)
        q.put((x, y))


def handle():
    while True:
        time.sleep(0.5)
        try:
            x, y = q.get(timeout=3)
        except:
            break
        else:
            print("%d + %d = %d" % (x, y, x + y))


p1 = Process(target=fun)
p2 = Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()
