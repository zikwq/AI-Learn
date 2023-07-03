# 链表结点实现
class SingLeNode():
    # 链表初始化
    def __init__(self,item):
        # item：存放元素
        self.item = item
        # next：表示下一个结点
        self.next = None


# 单链表的实现
class SingLeLinkList(object):
    def __init__(self,node=None):
        # head：首结点
        self.head = node

# 结点
node1 = SingLeNode(10)
print(node1.item)
print(node1.next)

# 链表
link1 = SingLeLinkList()
print(link1.head)
link2 = SingLeLinkList(node1)
print(link2.head.item)