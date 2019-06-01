"""

        共享内存
                Array(存放多个数值
"""
from multiprocessing import Array, Process
import time

# 创建共享内存
# 共享内存开辟5个整型列表空间
# shm = Array("i", 5)

# 共享内存初始化数据[1,2,3]
# shm = Array("i", [1, 2, 3])
#字节串
shm = Array("c", b"hello")


def fun():
    # 共享内存对象可迭代
    for i in shm:
        print(i)
    #修改共享内存
    # shm[1] = 1000
    shm[0]= b"H"
p = Process(target=fun)
p.start()
p.join()

for i in shm:
    print(i,end=" ")
print()
#通过value属性访问字节串
print(shm.value)