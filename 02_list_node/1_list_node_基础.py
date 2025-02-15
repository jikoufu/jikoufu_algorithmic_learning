class ListNode:
    """链表节点类"""

    def __init__(self, val: int):
        self.val: int = val  # 节点值
        self.next: ListNode | None = None  # 指向下一节点的引用


"""
1 -> 2 -> 4
在2后面添加3，首先需要记住4
因为添加的3需要连接到4
然后2链接3，或者3链接4
"""


def list_node_insert(n0: ListNode, P: ListNode):
    """在链表的节点 n0 之后插入节点 P"""
    n1 = n0.next
    P.next = n1
    n0.next = P


"""
1 -> 2 -> 4 ->3
删除3
首先需要记住3后面的
然后直接4链接3后面的
"""


def list_node_remove(n0: ListNode):
    """删除链表的节点 n0 之后的首个节点"""
    if not n0.next:
        return
    # n0 -> P -> n1
    P = n0.next
    n1 = P.next
    n0.next = n1

import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TestListNodeRemove(unittest.TestCase):
    def setUp(self):
        # 设置一个链表用于测试
        self.head = ListNode(1)
        self.head.next = ListNode(2)
        self.head.next.next = ListNode(3)

    def test_list_node_remove_NoNextNode_NoChange(self):
        # 测试只有一个节点的链表
        single_node = ListNode(1)
        list_node_remove(single_node)
        self.assertIsNone(single_node.next)

    def test_list_node_remove_MultipleNodes_RemovesNextNode(self):
        # 测试有多个节点的链表
        list_node_remove(self.head)
        self.assertEqual(self.head.val, 1)
        self.assertEqual(self.head.next.val, 3)
        self.assertIsNone(self.head.next.next)

    def test_list_node_remove_EndOfList_NoChange(self):
        # 测试移除最后一个节点之后的节点
        list_node_remove(self.head.next.next)
        self.assertEqual(self.head.val, 1)
        self.assertEqual(self.head.next.val, 2)


if __name__ == '__main__':
    unittest.main()
