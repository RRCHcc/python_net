"""

    僵尸进程
子进程先于父进程退出,父进程又没有处理子进程的退出状态,此时子进程就会称为
僵尸进程
"""
import os

pid = os.fork()
if pid < 0:
    pass
elif pid == 0:
    print("Child process", os.getpid())

else:
    while True:
        pass
