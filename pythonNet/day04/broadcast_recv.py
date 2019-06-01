"""

        UDP套接字广播（接收
1.创建udp套接字
2.选择接听端口
3.设置套接字为可以接收广播
"""
from socket import *

# 设置udp套接字
sockfd = socket(AF_INET, SOCK_DGRAM)
# 让套接字连接广播
sockfd.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sockfd.bind(("0.0.0.0", 44574))
while True:
    try:
        data, addr = sockfd.recvfrom(1024)
    except KeyboardInterrupt as e:
        break
    else:
        print("收到的消息：", data.decode())

sockfd.close()
