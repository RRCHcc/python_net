"""

        fork使用

"""
import os
import time

print("---------------------")
a = 1
pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:

    print("Child process")
    print("a:%d" % a)
    a = 10000
else:
    time.sleep(1)
    print("Parent process")
    print("a1:%d" % a)

print("All A =",a)