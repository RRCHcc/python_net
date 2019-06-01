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
        self.head = Node(None)#链表的开头

    def init_list(self,data):

        p = self.head          #可移动变量p
        for i in data:
            p.next = Node(i)
            p = p.next

    def show(self):
        p = self.head.next
        while p != None:
            print(p.val, end=" ")
            p = p.next
        print()

    #尾部插入新结点
    def append(self, total):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(total)
    #获取链表长度
    def get_length(self):
        count = 0
        p = self.head
        while p.next:
            count += 1
            p = p.next
        return count
    #判断链表是否为空
    def is_empty(self):
        if self.get_length()==0:#长度为0 就是空链表
            return True
        else:
            return False
    #清空链表
    def clear(self):
        self.head.next = None#切断头与后面元素的联系

    #根据结点获取相应值(获取索引值)
    def get_item(self,number):
        p = self.head
        if number > self.get_length():
            raise IndexError("list number out of range")
        for item in range(number+1):
            p = p.next
        return p.val
        # p = self.head.next
        # i = 0
        # while i < number and p is not None:
        #     i += 1
        #     p = p.next
        # if p is None
        #    raise IndexError("list number out of range")
        # else:
        #    return p.val

    #根据索引插入
    def insert(self, value, total):
        p = self.head
        q = Node(total)
        i = 0
        #判断是否超过范围
        if value < 0 or value >self.get_length():
            raise IndexError("list number out of range")
        while i < value:
            i += 1
            p = p.next
        q.next = p.next
        p.next = q
    #删除
    def delete(self,item):
        p = self.head
        while p.next is not None:
            if p.next.val == item:
                p.next = p.next.next
                break
            p = p.next
        else:
            raise ValueError("x not in list")


#创建链表对象
if __name__ =="__main__":
    link= LinkList()
    #初始数据
    l = [1,2,3,4,5]
    #将初始数据插入链表
    link.init_list(l)
    #实现在链表的尾部插入一个新的节点
    link.append(6)
    # 遍历链表
    link.show()
    link.insert(6, 10)
    link.show()
    print(link.get_length())
    # link.clear()
    link.show()
    print(link.is_empty())
    print(link.get_item(2))
    link.show()
    link.delete(5)
    link.show()

















