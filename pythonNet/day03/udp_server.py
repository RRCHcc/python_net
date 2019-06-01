"""
    UDP套接字服务端（重点代码）
            数据报套接字编程
    （面向无连接--udp协议--数据报套接字）
"""
from socket import *
#创建数据报套接字对象
sockfd = socket(AF_INET,SOCK_DGRAM)

#绑定地址
sockfd.bind(("0.0.0.0",44474))

#消息收发
while True:
    data, addr = sockfd.recvfrom(1024)
    print("收到的消息：",data.decode())
    result = input("GM:")
    n = sockfd.sendto(result.encode(),addr)

#关闭套接字
sockfd.close()
