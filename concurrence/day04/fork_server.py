"""

            基于fork的多进程网络并发模型
                        重点代码
实现步骤
1. 创建监听套接字
2. 等待接收客户端请求
3. 客户端连接创建新的进程处理客户端请求
4. 原进程继续等待其他客户端连接
5. 如果客户端退出,则销毁对应的进程

TCP套接字
"""
from socket import *
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
# tcp 套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 设置端口立即重用
# 绑定
s.bind(ADDR)
# 监听
s.listen(3)

# 僵尸进程的处理
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

print("Listen the port 44447...")
# 循环等待客户端连接
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue
    # 说明客户端连接 ,创建子进程处理客户端请求
    pid = os.fork()
    if pid == 0:
        s.close()  # 父进程不需要 s套接字
        handle(c)  # 通过函数具体处理客户端请求
        os._exit(0)  # 处理完客户端请求 退出
    # 父进程实际只用来处理客户端连接
    else:
        c.close()  # 父进程不需要 c套接字
