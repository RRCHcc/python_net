"""
        # 计算密集型函数,x y 传入1与1
编写程序完成效率测试，
使用单线程执行计算密集型函数十次
记录时间
执行io密集函数十次记录时间

使用十个线程分别执行计算密集函数1次
记录时间
执行io密集函数1次记录时间

"""
import time
from threading import Thread


def count(x, y):
    c = 0
    while c < 7000000:
        c += 1
        x += 1
        y += 1


# io 密集型
def io():
    write()
    read()


def write():
    f = open("test", "w")
    for i in range(1500000):
        f.write("hello world\n")
    f.close()


def read():
    f = open("test")
    lines = f.readlines()
    f.close()


jobs = []
a = time.time()
for i in range(10):
    t = Thread(target=count, args=(1, 1))
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()
b = time.time()
print(b - a)

# jobs01 = []
# a01 = time.time()
# for i in range(10):
#     t = Thread(target=io)
#     jobs01.append(t)
#     t.start()
# for i in jobs01:
#     i.join()
# b01 = time.time()
# print(b01 - a01)
#
# a02 = time.time()
# for i in range(10):
#    count(1, 1)
# b02 = time.time()
# print(b02 - a02)
#
# a03 = time.time()
# for i in range(10):
#     io()
# b03 = time.time()
# print(b03 - a03)
