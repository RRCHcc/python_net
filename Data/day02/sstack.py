"""

栈的顺序存储结构
重点代码
from 导入模块不能导入单下划线
"""
#自定义栈异常
class StackError(Exception):
    pass

#基于列表实现顺序栈
class SStack:
    def __init__(self):
    #约定 链表的最后一个元素为栈顶
        self._elems = []#_elems 当做普通变量

    def top(self):
        if not self._elems:
            raise StackError("stack is empty")
        return self._elems[-1]

    #判断是否为空，空为True
    def is_empty(self):
        return self._elems == []

    #入栈操作
    def push(self,elem):
        self._elems.append(elem)

    #出栈操作
    def pop(self):
        if not self._elems:
            raise StackError("stack is empty")
        return self._elems.pop()



if __name__ == "__main__":
    st = SStack()#初始化
    # print(st.top())
    # print(st.is_empty())
    # st.push(1)
    # st.push(2)
    # st.push(3)
    # while not st.is_empty():
    #     print(st.pop())
    data = "asdf (asd(fasd) {fasd [af] fasd} fas asd sd as "

    for i in data:
        if i == "(" or i == "[" or i == "{":
            st.push(i)
        elif i == ")" or i == "]" or i == "}":
            st.pop()
    print(st.is_empty())


























