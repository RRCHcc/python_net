"""
http 功能演示
将网页发送给浏览器展示
"""
from socket import *


def handle(connfd):
    print("Request from", connfd.getpeername())
    request = connfd.recv(4096)  # 接收 http 请求
    # 防止客户端断开
    if not request:
        return
    # 将request按行分割
    request_line = request.splitlines()[0].decode()
    # 获取请求内容
    info = request_line.split(" ")[1]
    # 判断获取内容是否为 “ / ”
    if info == "/":
        f = open("index.html")
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html\r\n"
        response += "\r\n"
        response += f.read()
    else:
        response = "HTTP/1.1 404 NOT Found\r\n"
        response += "Content-Type: text/html\r\n"
        response += "\r\n"
        response += "<h1>Sorry   ~.~!!!!....<h1>"
        # 向浏览器发送内容
    connfd.send(response.encode())


# 搭建TCP网络
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(("0.0.0.0", 44444))
    sockfd.listen(3)
    print("Listen the port 44444....")
    while True:
        connfd, addr = sockfd.accept()
        handle(connfd)  # 处理浏览器回收
        connfd.close()


if __name__ == "__main__":
    main()
