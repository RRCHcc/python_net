"""
套接字属性
"""
from socket import *
#创建一个tcp套接字
s = socket()

#设置套接字端口立即重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)

s.bind(("0.0.0.0", 44744))
s.listen(3)
c,addr = s.accept()
print("!!")
c.recv(1024)

print("套接字地址类型：",s.family)
print("套接字类型：",s.type)
print("套接字地址类型：",s.getsockname())
print("套接字描述符：",s.fileno())
print("套接字客户端地址：",c.getpeername())#连接套接字调用













