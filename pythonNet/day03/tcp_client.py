"""
    TCP套接字客户端（重点代码）
            流式套接字编程
    （面向连接--tcp协议--可靠的--流式套接字）
不在一个主机要用网络地址
"""
from socket import *

# 创建套接字对象
sockfd = socket()

# 发起连接
serber_addr = ("176.140.6.123", 44474)
sockfd.connect(serber_addr)

# 消息收发

while True:
    result = input("请输入：")
    # 得到空则退出循环
    if not result:
        break
    sockfd.send(result.encode())
    data = sockfd.recv(1024)
    print("From server", data.decode())

# 关闭
sockfd.close()
