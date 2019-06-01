"""
服务端部分
处理逻辑请求
"""
from socket import *
from multiprocessing import Process
import signal
import sys
from operation_db import *

# 全局变量
HORT = "0.0.0.0"
PORT = 44447
ADDR = (HORT, PORT)


# 处理登录
def do_login(c, db, data):
    tmp = data.split(' ')
    name = tmp[1]
    passwd = tmp[2]

    # 到数据库进行判断
    if db.login(name, passwd):
        c.send(b"OK")
    else:
        c.send(b"FAIL")


# 处理注册
def do_register(c, db, data):
    tmp = data.split(' ')
    name = tmp[1]
    passwd = tmp[2]

    if db.register(name, passwd):
        c.send(b"OK")
    else:
        c.send(b"FAIL")


# 处理查询
def do_query(c, db, data):
    tmp = data.split(' ')
    name = tmp[1]
    word = tmp[2]

    # 插入历史记录
    db.insert_history(name, word)
    # 查单词    没查到返回none
    mean = db.query(word)
    if not mean:
        c.send("没有找到该单词".encode())
    else:
        msg = "%s : %s" % (word, mean)
        c.send(msg.encode())



# 查询历史记录
def do_history(c, db, data):
    tmp = data.split(' ')
    name = tmp[1]

    mean = db.history(name)
    if not mean:
        c.send(b"FAIL")
    else:
        c.send(b'OK')
        for i in mean:
            # i ===> (name word time)
            msg = "%s  %s  %s" % i
            time.sleep(0.1)  # 防止沾包
            c.send(msg.encode())

        time.sleep(0.1)
        c.send(b"##")


# 处理客户端请求
def do_request(c, db):
    db.create_cursor()  # 生成游标 db.cur
    while True:
        data = c.recv(1024).decode()
        print(c.getpeername(), ":", data)
        if not data or data[0] == 'E':
            # db.close()
            c.close()
            sys.exit("客户端退出")
        elif data[0] == 'R':
            do_register(c, db, data)
        elif data[0] == 'L':
            do_login(c, db, data)
        elif data[0] == 'Q':
            do_query(c, db, data)
        elif data[0] == 'H':
            do_history(c, db, data)


# 网络搭建
def main():
    # 创建数据库对象
    db = Database()

    # 创建tcp套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    print("Listen the port 44447")

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    while True:
        try:
            c, addr = s.accept()
            print("Connect from :", addr)
        except KeyboardInterrupt:
            s.close()
            db.close()
            sys.exit("服务器关闭")
        except Exception as e:
            print(e)
            continue
        # 创建子进程
        p = Process(target=do_request, args=(c, db))
        p.daemon = True
        p.start()


if __name__ == '__main__':
    main()
