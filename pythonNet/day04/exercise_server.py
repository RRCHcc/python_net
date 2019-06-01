"""
练习
从客户端输入一个学生的id 姓名 年龄 分数
将其发送到服务端，有服务端写入到一个文件
每个信息占一行
数据传输使用udp套接字完成
                        服务端
"""
from socket import *
import struct

sockfd = socket(AF_INET, SOCK_DGRAM)
sockfd.bind(("0.0.0.0", 44474))
# 确定数据结构
st = struct.Struct("i32sif")
# 打开文件
fd = open("student.txt", "a+")
while True:
    data, addr = sockfd.recvfrom(1024)
    # 数据解析
    data = st.unpack(data)
    info = "%d %s %d %.2f\n" % (data[0],
                                data[1].decode(),
                                data[2],
                                data[3])
    fd.write(info)

fd.close()
sockfd.close()
