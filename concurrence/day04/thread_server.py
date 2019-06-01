"""

            基于threading的多线程网络并发
                        重点代码
1. 创建监听套接字
2. 循环接收客户端连接请求
3. 当有新的客户端连接创建线程处理客户端请求
4. 主线程继续等待其他客户端连接
5. 当客户端退出,则对应分支线程退出
"""
from socket import *
from threading import Thread
import os, sys



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
    t = Thread(target=handle, args=(c,))
    t.setDaemon(True)  # 分支线程随主线程退出
    t.start()
