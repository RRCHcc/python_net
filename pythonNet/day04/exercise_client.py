"""
练习
从客户端输入一个学生的id 姓名 年龄 分数
将其发送到服务端，有服务端写入到一个文件
每个信息占一行
数据传输使用udp套接字完成
                        客户端
"""
from socket import *
import struct

HOST = "127.0.0.1"
PORT = 44474
ADDR = (HOST, PORT)
sockfd = socket(AF_INET, SOCK_DGRAM)
# 跪地数据格式
st = struct.Struct("i32sif")
while True:
    print("-------------------")
    id = int(input("请输入id>>"))
    name = input("请输入姓名>>")
    age = int(input("请输入年龄>>"))
    score = float(input("请输入分数>>"))

    # 数据打包
    info = st.pack(id, name.encode(), age, score)
    sockfd.sendto(info, ADDR)

sockfd.close()
