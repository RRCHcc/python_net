"""
面试类型：
        通过完成上面的MyTread类让整个程序可以正常执行
        当条用start是player作为一个线程功能函数执行
        注意，函数的名称和参数并不确定，player只是测试函数

"""
from threading import Thread
from time import sleep, ctime


class MyThread(Thread):
    def __init__(self, target=None, args=(), kwargs={}, name=None):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.name = name

    def run(self):
        self.target(*self.args, **self.kwargs)


def player(sec, song):
    for i in range(5):
        print("Playing %s:%s" % (song, ctime()))
        sleep(sec)


t = MyThread(target=player, args=(3,),
             kwargs={"song": "凉凉"}, name=" qtx")

t.start()
t.join()
