"""
        IO多路复用
            poll 方法实现多客户端通信
                次重点
"""
from select import *
from socket import *

# 创建关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 44447))
s.listen(5)

# 创建poll
p = poll()

# 创建查找字典{fileno：io对象,}
fdmap = {s.fileno(): s}

# 设置关注io
p.register(s, POLLIN | POLLERR)

# 循环监控io发生
while True:
    events = p.poll()  # 阻塞等待io发生
    # 遍历列表处理IO
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("Connect from", addr)
            # 添加新的关注事件
            p.register(c, POLLIN | POLLHUP)
            fdmap[c.fileno()] = c
        # elif event & POLLHUP:  # 当断开事件发生时，POLLIN也会就绪
        #     print("客户端退出", addr)
            # p.unregister(fd)  # 取消关注
            # fdmap[fd].close()
            # del fdmap[fd]  # 从字典删除

        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)  # 取消关注
                fdmap[fd].close()
                del fdmap[fd]  # 从字典删除
                continue
            print(data.decode())
            fdmap[fd].send(b"OK")
