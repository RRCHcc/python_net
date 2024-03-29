"""

    自定义线程类

"""
from threading import Thread


class MyThread(Thread):
    def __init__(self, attr):
        self.attr = attr
        super().__init__()

    # 多个方法配合实现具体功能
    def f1(self):
        print("步骤1", self.attr)

    def f2(self):
        print("步骤2")

    def run(self):
        self.f1()
        self.f2()


t = MyThread("XXXXXX")
t.start()
t.join()
