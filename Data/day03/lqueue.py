"""
队列的链式存储结构
重点代码
"""
#自定义队列异常
class LqueueError(Exception):
    pass

#创建结点类
class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

class LQqueue:
    def __init__(self):
        # self._top = Node(None)
        self.front = self. rear = Node(None)
    #判断是否为空
    def is_empty(self):
        return self.front == self.rear
        # return self._top is None

    #入队
    def enqueue(self, elem):
        # p = self._top
        # while p.next is not None:
        #     p = p.next
        # p.next = Node(elem)
        self.rear.next = Node(elem)
        self.rear = self.rear.next

    #出队
    def dequeue(self):
        if self.is_empty():
            raise LqueueError("lqueue is empty")
        # p = self._top.next.val
        # self._top.next = self._top.next.next
        # return p
        self.front = self.front.next
        return self.front.val

    #将队列清空
    def clear(self):
        self.rear = self.front

if __name__ =="__main__":
    lq = LQqueue()
    print(lq.is_empty())
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    lq.enqueue(40)
    lq.enqueue(50)
    while not lq.is_empty():
        print(lq.dequeue())



