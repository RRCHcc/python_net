"""
    UDP套接字客户端（重点代码）
            数据报套接字编程
    （面向无连接--udp协议--数据报套接字）
"""
from socket import *
#服务器地址
HOST = "127.0.0.1"
PORT = 44474
ADDR = (HOST,PORT)
#创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#收发消息
while True:
    result = input("MSG>>>")
    if not result:
        break
    sockfd.sendto(result.encode(), ADDR)
    msg, data = sockfd.recvfrom(1024)
    print("From server",msg.decode())

#关闭
sockfd.close()
