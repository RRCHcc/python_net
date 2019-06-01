"""

        fork使用

"""
import os
import time

pid = os.fork()
if pid < 0:
    print("Create process failed")
elif pid == 0:
    time.sleep(5)
    print("The new process")
else:
    time.sleep(6)
    print("The old process")

print("Fork test over")
