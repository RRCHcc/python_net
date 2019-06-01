


from squeue import*
class TreeNode:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class Bittree:
    def __init__(self,root = None):
        self.root = root    #起始根


    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False
    #先序
    def preOrder(self,node):
        if node is None:
            return
        print(node.data,end=" ")
        self.preOrder(node.left)
        self.preOrder(node.right)

    # 中序
    def inOrder(self,node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.data,end=" ")
        self.inOrder(node.right)

    # 后序
    def postOrder(self,node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data,end=" ")
    #层次遍历,利用队列的概念，让根进队，出队的时候让其左右进队
    def levelOrder(self,node):
        qu = SQueue()
        qu.enqueue(node)#先将根节点入队
        while not qu.is_empty():
            node = qu.dequeue()
            print(node.data,end=" ")
            if node.left:#判断左右是否为空
                qu.enqueue(node.left)
            if node.right:
                qu.enqueue(node.right)


if __name__ =="__main__":
    b = TreeNode("B")
    f = TreeNode("F")
    g = TreeNode("G")
    d = TreeNode("D", f, g)
    i = TreeNode("I")
    h = TreeNode("H")
    e = TreeNode("E", i, h)
    c = TreeNode("C", d, e)
    a = TreeNode("A", b, c)   #根结点

    bt = Bittree(a)     #初始化树对象，传入根结点
    #先序遍历
    # print("preOrder")
    # bt.preOrder(bt.root)
    # print()
    # bt.inOrder(bt.root)
    # print()
    # bt.postOrder(bt.root)
    bt.levelOrder(bt.root)