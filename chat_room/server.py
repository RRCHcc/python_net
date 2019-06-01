"""

                    服务端
功能 : 类似qq群功能
【1】 有人进入聊天室需要输入姓名,姓名不能重复
【2】 有人进入聊天室时,其他人会收到通知:xxx 进入了聊天室
【3】 一个人发消息,其他人会收到:xxx : xxxxxxxxxxx
【4】 有人退出聊天室,则其他人也会收到通知:xxx退出了聊天室
【5】 扩展功能:服务器可以向所有用户发送公告:管理员消息: xxxxxxxxx
"""
from socket import *
import os

# 创建网络连接

# 服务器地址
ADDR = ("0.0.0.0", 44447)
# 存储用户信息
user = {}


def do_login(s, name, addr):
    if name in user or "管理员" in name:
        s.sendto("\n该用户已存在".encode(), addr)
        return

    s.sendto(b"OK", addr)

    # 通知其他用户
    msg = "\n欢迎%s进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])

    # 将用户信息加入字典
    user[name] = addr


def do_chat(s, name, text):
    msg = "%s : %s" % (name, text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])


# 退出
def do_quit(s, name):
    msg = "\n%s退出了聊天室" % name
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])
        else:
            s.sendto(b"EXIT", user[i])
    # 将用户删除
    del user[name]


# 接收客户端请求
def do_request(s):
    while True:
        data, addr = s.recvfrom(1024)
        msg = data.decode().split(" ")
        # 区分请求类型
        if msg[0] == "L":
            do_login(s, msg[1], addr)
        elif msg[0] == "C":
            text = " ".join(msg[2:])
            do_chat(s, msg[1], text)
        elif msg[0] == "Q":
            if msg[1] not in user:
                s.sendto(b"EXIT",addr)
                continue
            do_quit(s, msg[1])


def main():
    # 套接字
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)

    pid = os.fork()
    if pid < 0:
        return
    # 发送管理员消息
    elif pid == 0:
        while True:
            msg = input("管理员消息：")
            msg = "C 管理员消息 " + msg
            s.sendto(msg.encode(), ADDR)
    else:
        # 接收请求
        do_request(s)  # 处理客户端请求


if __name__ == "__main__":
    main()
