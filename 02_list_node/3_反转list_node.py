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



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_between(head, left, right):
    if not head or left == right:
        return head  # 特殊情况：空链表 or 不需要反转

    dummy = ListNode(0)  # 虚拟头节点，方便操作
    dummy.next = head
    prev = dummy  # prev 最终会指向 before_left

    # **1. 找到 left 前面的节点（before_left）**
    for _ in range(left - 1):
        prev = prev.next

    before_left = prev   # 记录 left 之前的节点
    left_node = prev.next  # left 节点（即要反转的部分）

    # **2. 反转 left 到 right 之间的部分**
    prev = None
    curr = left_node
    for _ in range(right - left + 1):
        next_node = curr.next
        curr.next = prev  # 反转指针
        prev = curr
        curr = next_node

    # **3. 重新连接反转后的部分**
    before_left.next.next = curr  # 让反转后的尾部（原来的 left）连接 right 之后的部分
    before_left.next = prev  # 让 left 之前的部分连接反转后的头部（原来的 right）

    return dummy.next  # 返回新的头节点
