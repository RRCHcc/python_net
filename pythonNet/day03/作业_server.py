"""

使用tcp服务端和客户端编程，
将一个文件从客户端发送到服务端，
文件类型为图片或者普通文本皆可

    while True:
        time.sleep(0.1)
        data = fd.readline(27)
        if not data:
            break
        sockfd.send(data)
"""
from socket import *

#创建套接字对象
sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR, True)

#绑定地址
sockfd.bind(("0.0.0.0", 44444))

#设置监听
sockfd.listen(5)

#等待处理客户端连接请求
            #connfd 客户端连接套接字
            # addr 连接的客户端地址
while True:
    print("等待接受文件....")
    try:
        connfd, addr = sockfd.accept()
        print("Connect from:", addr)
    except KeyboardInterrupt:
        print("退出服务")
        break
    #收发消息

    while True:
        data = connfd.recv(1024)
        # 得到空则退出循环
        if not data:
            break
        fd = open("get_file", "ab+")
        fd.write(data)
    connfd.close()
#关闭套接字
fd.close()
sockfd.close()


