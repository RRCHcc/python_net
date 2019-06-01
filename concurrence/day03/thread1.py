"""

        线程编程(Thread)
示例
"""
from threading import Thread
import time
import os

a = 1


# 线程函数
def music():
    global a
    print("a= ",a)
    a = 10000
    for i in range(5):
        time.sleep(2)
        print(os.getpid(), "播放心如刀割")


# 创建线程
t = Thread(target=music)
t.start()

# 创建主线程
for i in range(5):
    time.sleep(3)
    print(os.getpid(), "哈哈哈")

t.join()
print(a)

