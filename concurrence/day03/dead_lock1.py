"""

        死锁及其处理
RLock 重载锁， 允许重复上锁
"""
from threading import Thread, RLock
import time

num = 0  # 模拟共享资源
lock = RLock()  #在一个线程内可以对锁进行重复加锁


class MyThread(Thread):
    def fun(self):
        global num
        with lock:
            num -= 1

    def fun2(self):
        global num
        if lock.acquire():
            num += 1
            if num > 5:
                self.fun()
            print("NUM = ", num)
            lock.release()

    def run(self):
        time.sleep(2)
        self.fun2()

for i in range(10):
    t = MyThread()
    t.start()

