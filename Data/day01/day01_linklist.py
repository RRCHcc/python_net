"""

        链式结构代码实现

**重点程序**

链式线性思路
1.结点如何表示？
	自定义对象:对象即数据，对象属性即数据元素
	数据元素：包含有用数据和记录下一个对象地址的数据
2.如何建立关联？
a = Node(1)  a.val = 1 a.next = b
b = Node(2)  b.val = 2 b.next = None
3.实现什么样的链表操作？
        链表初始化
        链表的遍历
"""

#创建结点类
class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

#链表的操作
class LinkList:
    def __init__(self):
        self.head = None

    def init_list(self,data):
        self.head = Node(None)#链表的开头
        p=self.head          #可移动变量p
        for i in data:
            p.next = Node(i)
            p = p.next

    def show(self):
        p = self.head.next
        while p!=None:
            print(p.val,end="")
            p = p.next
        print()

    def append(self,total):
        p = self.head
        while p.next!=None:
            p = p.next
        p.next = Node(total)

    def my_insert(self,value,total):
        p = self.head
        q = Node(total)
        while p.val != value:
            p = p.next
        q.next = p.next
        p.next = q



#创建链表对象
if __name__ =="__main__":
    link= LinkList()

    #初始数据
    l = [1,2,3]
    #将初始数据插入链表
    link.init_list(l)
    #实现在链表的尾部插入一个新的节点
    link.append(7)
    # 遍历链表
    link.show()
    link.my_insert(3,8)
    link.show()















