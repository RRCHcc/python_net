from socket import *

#创建套接字对象
sockfd = socket()

#发起连接
serber_addr = ("176.140.6.123",44444)
sockfd.connect(serber_addr)

#消息收发
result = input("请输入需要传输文件：")
fd = open(result,"rb")
while True:
    data = fd.read(1024)
    if not data:
        break
    sockfd.send(data)

#关闭
fd.close()
sockfd.close()