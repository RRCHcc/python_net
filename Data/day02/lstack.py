"""
栈的链式存储结构
重点代码
"""
#自定义栈异常
class StackError(Exception):
    pass

#创建结点类
class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

class LStack:
    def __init__(self):
        self._top = None  # 标记栈顶位置

    def is_empty(self):
        return self._top is None

    def push(self,elem):
        # node = Node(elem,)
        # node.next = self.top
        # self.top = node
        self._top = Node(elem, self._top)

    def pop(self):
        if self.top is None:
            raise StackError("stac is empty")
        p = self._top
        self._top = p.next
        return p.val

    def top(self):
        if self._top is None:
            raise StackError("stac is empty")
        return self._top.val
    #将栈清空
    def clear(self):
        self.top = None



if __name__ == "__main__":
    st = LStack()
    print(st.is_empty())
    st.push(10)
    st.push(20)
    st.push(30)
    print(st.top())
    while not st.is_empty():
        print(st.pop())









