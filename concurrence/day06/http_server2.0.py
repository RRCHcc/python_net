"""
http 2.0升级版本
    *io并发处理
    *基本的requert解析
    *使用类封装
升级点 :
【1】采用IO并发,可以满足多个客户端同时发起请求情况
【2】做基本的请求解析,根据具体请求返回具体内容,同时
    满足客户端简单的非网页请求情况
【3】通过类接口形式进行功能封装
"""
from socket import *
from select import select


# 将具体http server功能封装
class HTTPSever:
    def __init__(self, server_addr, static_dir):
        self.server_addr = server_addr
        self.static_dir = static_dir
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.creata_soket()
        self.bind()

    # 创建套接字
    def creata_soket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self):
        self.sockfd.bind(self.server_addr)
        self.ip = self.server_addr[0]
        self.port = self.server_addr[1]

    # 启动服务
    def server_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d" % self.port)
        self.rlist.append(self.sockfd)
        while True:
            rs, ws, xs = select(self.rlist,
                                self.wlist,
                                self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    print("Connect from", addr)
                    self.rlist.append(c)
                else:  # 处理浏览器请求
                    self.handle(r)

    def handle(self, connfd):
        # 接收http请求
        request = connfd.recv(4096)
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return

        # 请求解析
        request_line = request.splitlines()[0]
        info = request_line.decode().split(" ")[1]
        print(connfd.getpeername(), ":", info)
        # info 如果分为访问网页和其他
        if info == "/" or info[-5:] == ".html":
            self.get_html(connfd, info)
        else:
            self.get_data(connfd,info)

        self.rlist.remove(connfd)
        connfd.close()
    # 其他请况
    def get_data(self,connfd,info):
        responseHeaders = "Http/1.1 200 OJ8K\r\n"
        responseHeaders += "\r\n"
        responseBody = "<h1>Waiting httpserver3.0<h1>"
        response = responseHeaders+responseBody
        connfd.send(response.encode())
    # 处理网页
    def get_html(self, connfd, info):
        if info == "/":
            # 网页文件
            filenaem = self.static_dir + "/index.html"
        else:
            filenaem = self.static_dir + info
        try:
            fd = open(filenaem)
        except Exception:
            # 没有网页返回404
            responseHeaders = "Http/1.1 404 Not Found\r\n"
            responseHeaders += "\r\n"
            responseBody = "<h1>Sorry,Not Found the page<h1>"
        else:
            responseHeaders = "Http/1.1 200 OK\r\n"
            responseHeaders += "\r\n"
            responseBody = fd.read()
        finally:
            response = responseHeaders + responseBody
            connfd.send(response.encode())


# 如何使用httpsever类
if __name__ == "__main__":
    # 用户自己决定：地址 ,内容
    server_addr = ("0.0.0.0", 44474)
    static_dir = "./static"  # 网页存放位置

    httpd = HTTPSever(server_addr, static_dir)  # 生成实例对象
    httpd.server_forever()  # 启动服务

