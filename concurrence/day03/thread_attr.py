"""

    线程对象属性

"""
from threading import Thread
import time


def fun():
    time.sleep(3)
    print("线程属性测试")


t = Thread(target=fun, name="Wahaha")

t.setDaemon(True)

t.start()
# 线程名称
t.setName("惨兮兮")
print("Thread name", t.getName())
print(t.is_alive())
