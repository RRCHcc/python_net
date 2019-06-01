"""

队列的顺序存储结构
重点代码
from 导入模块不能导入单下划线
"""
#自定义队列异常
class QueueError(Exception):
    pass

#基于列表实现顺序队列
class SQueue:
    def __init__(self):
    #约定 队列第一个元素为队头，最后一个元素为队尾
        self._elems = []#_elems 当做普通变量
    #入队
    def enqueue(self,item):
        self._elems.append(item)
    #出队
    def dequeue(self):
        if not self._elems:
            raise QueueError("queue is empty")
        return self._elems.pop(0)

    def top(self):
        if not self._elems:
            raise QueueError("queue is empty")
        return self._elems[0]

    def is_empty(self):
        return self._elems == []

if __name__ == "__main__":
    sq = SQueue()
    sq.enqueue(10)
    sq.enqueue(11)
    sq.enqueue(12)
    while not sq.is_empty():
        print(sq.top())
        print(sq.dequeue())