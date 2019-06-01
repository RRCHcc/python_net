"""
HTTP请求
request
HTTP响应
response
"""
from socket import *

# 创建tcp套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)

s.bind(("0.0.0.0", 44444))
s.listen(3)

c, addr = s.accept()
print("Conner from", addr)
data = c.recv(4096)
print(data)
# http 响应格式
data = """http/1.1 200 OK
Content-Type/html

<h1>hello world</h1>
"""
c.send(data.encode())
c.close()
s.close()
