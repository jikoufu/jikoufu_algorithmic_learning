"""
1. 双指针的核心思想
双指针通过两个变量指向不同位置，并根据特定规则移动指针，以减少不必要的遍历，提高效率。
常见的双指针类型：

对撞指针（Two-way Pointers） → 适用于排序数组或字符串处理
快慢指针（Fast & Slow Pointers） → 适用于链表问题，如检测环
滑动窗口（Sliding Window） → 适用于子数组问题，如求最小覆盖子串
"""


# (1) 对撞指针：适用于排序数组或字符串
"""
示例1：两数之和（输入已排序数组）
题目：给定有序数组 nums，找到两个数，使其和等于 target，返回索引（假设有唯一解）。

思路：

使用左指针 left = 0 和 右指针 right = len(nums) - 1
如果 nums[left] + nums[right] == target，返回索引
如果和小于 target，移动 left++
如果和大于 target，移动 right--
"""


def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left,right]
        elif total< target:
            left += 1
        else:
            right -= 1

    return []

"""
示例2：寻找环的起点
题目：如果链表有环，返回环的起点节点。

思路：

先用快慢指针判断是否有环（如上）。
如果有环，让 其中一个指针回到起点，另一个指针停留在相遇点。
两个指针每次走一步，相遇时即为环的起点。
"""
def detect_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # 有环
            slow = head  # 重新指向链表头
            while slow != fast:  # 重新遍历找环起点
                slow = slow.next
                fast = fast.next
            return slow
    return None  # 无环

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TestDetectCycle:
    def test_detect_cycle_EmptyList_ReturnsNone(self):
        head = None
        assert detect_cycle(head) is None

    def test_detect_cycle_NoCycle_ReturnsNone(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        assert detect_cycle(head) is None

    def test_detect_cycle_CycleAtHead_ReturnsHead(self):
        head = ListNode(1)
        head.next = head
        assert detect_cycle(head) == head

    def test_detect_cycle_CycleInMiddle_ReturnsCycleStart(self):
        head = ListNode(1)
        head.next = ListNode(2)
        cycle_start = ListNode(3)
        head.next.next = cycle_start
        cycle_start.next = ListNode(4)
        cycle_start.next.next = cycle_start
        assert detect_cycle(head) == cycle_start

    def test_detect_cycle_CycleAtEnd_ReturnsCycleStart(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        cycle_start = ListNode(4)
        head.next.next.next = cycle_start
        cycle_start.next = ListNode(5)
        cycle_start.next.next = cycle_start
        assert detect_cycle(head) == cycle_start
