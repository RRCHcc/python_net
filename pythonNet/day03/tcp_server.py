"""
    TCP套接字服务端（重点代码）
            流式套接字编程
    （面向连接--tcp协议--可靠的--流式套接字）

"""
from socket import *
#创建套接字对象
sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)

#绑定地址
sockfd.bind(("0.0.0.0", 44444))

#设置监听
sockfd.listen(5)

#等待处理客户端连接请求
            #connfd 客户端连接套接字
            # addr 连接的客户端地址
while True:
    print("Waiting for connect....")
    try:
        connfd, addr = sockfd.accept()
        print("Connect from:", addr)
    except KeyboardInterrupt:
        print("退出服务")
        break
    #收发消息
    while True:
        data = connfd.recv(1024)
        #得到空则退出循环
        if not data:
            break
        print("接受的消息：", data.decode())

        n = connfd.send("收到".encode())
        print("发送了%d个字节数据" % n)
    connfd.close()
#关闭套接字

sockfd.close()

















