"""
        gevent模块
"""
import gevent


def foo(a, b):
    print("Running foo...", a, b)
    gevent.sleep(2)
    print("Foo again..")


def bar():
    print("Running bar....")
    gevent.sleep(3)
    print("Bar again")


# 将函数封装为协程，遇到gevent阻塞自动执行
f = gevent.spawn(foo, 1, "hello")
g = gevent.spawn(bar)

gevent.joinall([f, g])  # 等待 f ，g 结束
