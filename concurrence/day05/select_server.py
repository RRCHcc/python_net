"""
        IO多路复用
            select 方法实现多客户端通信
                重点代码
"""
from select import select
from socket import *

# 设置套接字为关注IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口重复利用
s.bind(("0.0.0.0", 44744))
s.listen(5)

# 设置关注的IO
rlist = [s, ]
wlist = []
xlist = []

while True:
    # 监控IO的发生
    rs, ws, xs = select(rlist, wlist, xlist)
    # 遍历三个返回值列表，判断那个IO发生
    for r in rs:
        # 如果是套接字就绪，处理连接
        if r is s:
            c, addr = r.accept()
            print("Connect from", addr)
            rlist.append(c)  # 加入新的关注IO
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                continue
            print(data.decode())
            # r.send(b"OK")
            # 希望我们主动处理这个IO
            wlist.append(r)
    for w in ws:
        w.send(b"OJ8K")
        wlist.remove(w)
    for x in xs:
        pass
