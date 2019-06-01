"""


"""
from socket import *
from multiprocessing import Process
import os, sys
import signal


def handle(c):
    print("客户端：", c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"OK")
    c.close()


# 创建监听套接字
HOST = "0.0.0.0"
PORT = 44447
ADDR = (HOST, PORT)

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)

# 僵尸进程处理
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print("Listen the port 44447...")

# 循环等待客户端连接
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("退出服务器")  # 退出进程
    except Exception as e:
        print(e)
        continue

    # 创建新的线程处理客户端请求
    p = Process(target=handle, args=(c,))
    p.daemon = True  # 分支线程随主线程退出
    p.start()
