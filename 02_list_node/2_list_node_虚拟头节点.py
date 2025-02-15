import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    # 创建一个虚拟头节点，以处理删除头节点的情况
    dummy = ListNode(next=head)
    current = dummy

    while current.next:
        if current.next.val == val:
            current.next = current.next.next  # 删除节点
        else:
            current = current.next  # 移动指针

    return dummy.next  # 返回新的头节点





