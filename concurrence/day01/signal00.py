"""

信号方法处理僵尸

"""
import os
import signal

# 处理子进程退出
#子进程发出退出信号后父进程进行忽略
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    print("haha", os.getpid())
else:
    while True:
        pass
