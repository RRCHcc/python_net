"""

            线程同步互斥方法
        线程Event
"""
from threading import Event
from threading import Thread
import time

s = None  # 全局变量用于通信
e = Event()  # 事件对象


def 杨子荣():
    print("大嫂杨子荣前来接你回家啦")
    global s
    s = "天王盖地虎"
    e.set()  # 共享资源操作完毕


t = Thread(target=杨子荣)
t.start()
e.wait()  # 阻塞等待
print("说对口令才是自己人")
if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
else:
    print("打死你个龟孙")

t.join()
