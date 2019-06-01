"""

    pid 进程相关函数

"""
import os

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Child pid", os.getpid())
    print("Get parent pid", os.getppid())

else:
    print("Parent pid", os.getpid())
    print("Get child pid", pid)
