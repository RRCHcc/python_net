"""

    pid 进程相关函数

"""
import os
import sys
pid = os.fork()
# os._exit(2)#进程退出
sys.exit("进程退出")

print("Process exit")

