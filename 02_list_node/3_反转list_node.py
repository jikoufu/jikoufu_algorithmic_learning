class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head

    while curr:
        next_temp = curr.next  # 暂时保存当前节点的下一个节点
        curr.next = prev  # 反转当前节点的指针
        prev = curr  # 移动 prev 指针到当前节点
        curr = next_temp  # 移动 curr 指针到下一个节点

    return prev  # prev 是新的头节点
