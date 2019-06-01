"""
客户端
"""
from socket import *
import sys, time


# 具体功能

class FtpClient:
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b"L")  # 发送请求
        # 等待回复
        data = self.sockfd.recv(128).decode()
        # ok 表示请求成功
        if data == "OK":
            data = self.sockfd.recv(128)
            print(data.decode())
        else:
            print(data)

    def do_quit(self):
        self.sockfd.send(b"Q")
        self.sockfd.close()
        sys.exit("谢谢使用")

    def do_get(self, filename):
        # 发送请求
        self.sockfd.send(("G " + filename).encode())
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == "OK":
            fd = open(filename, "wb")
            while True:
                data = self.sockfd.recv(1024)
                if data == b"##":
                    break
                fd.write(data)
        else:
            print(data)

    def do_put(self, filename):

        # 判断是否有该文件
        try:
            f = open(filename, "rb")
        except Exception:
            print("没有该文件")
            return

            # 发送请求
        filename = filename.split("/")[-1]
        self.sockfd.send(("P " + filename).encode())

        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == "OK":
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            f.close()
        else:
            print(data)


def request(sockfd):
    ftp = FtpClient(sockfd)

    while True:
        print("\n--------命令  选项----------")
        print("-----------  list  ---------")
        print("-----------get file---------")
        print("-----------put file---------")
        print("-----------  quit  ---------")
        cmd = input("请输入命令：")
        if cmd.strip() == "list":
            ftp.do_list()

        elif cmd[:3] == "get":
            filename = cmd.strip().split(" ")[-1]
            ftp.do_get(filename)

        elif cmd[:3] == "put":
            filename = cmd.strip().split(" ")[-1]
            ftp.do_put(filename)

        elif cmd.strip() == "quit":
            ftp.do_quit()


# 网络连接
def main():
    # 服务器地址
    ADDR = ("176.140.6.133", 54321)
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print("连接服务器失败")
        return
    else:
        print("""
        *****************************
            Data    File    Image
        *****************************
        """)
        cls = input("请输入文件种类：")
        if cls not in ["Data", "File", "Image"]:
            print("Sorry input Error")
            return
        else:
            sockfd.send(cls.encode())
            request(sockfd)  # 发送具体请求


if __name__ == "__main__":
    main()
