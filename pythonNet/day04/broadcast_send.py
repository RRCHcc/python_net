"""

        UDP套接字广播(发送

"""
from socket import *
import time
sockfd =socket(AF_INET,SOCK_DGRAM)
#广播地址
dest = ("176.140.6.255",44574)
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    time.sleep(1)

    result = """
    *******************
    ～～激情时刻～～～
    *******************
    """
    sockfd.sendto(result.encode(),dest)
