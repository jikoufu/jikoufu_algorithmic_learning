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
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1

    return []


import unittest


class TestTwoSum(unittest.TestCase):
    def test_two_sum_FoundPair_ReturnsIndices(self):
        self.assertEqual(two_sum([1, 2, 3, 4, 5], 9), [3, 4])
        self.assertEqual(two_sum([1, 2, 3, 4, 5], 8), [2, 4])

    def test_two_sum_NoPair_ReturnsEmptyList(self):
        self.assertEqual(two_sum([1, 2, 3, 4, 5], 10), [])
        self.assertEqual(two_sum([1, 2, 3, 4, 5], 0), [])

    def test_two_sum_EdgeCases_ReturnsEmptyList(self):
        self.assertEqual(two_sum([1], 1), [])
        self.assertEqual(two_sum([], 0), [])


"""
示例2：判断回文字符串
题目：给定字符串 s，判断是否是回文（忽略非字母数字字符，忽略大小写）。

思路：

左指针 指向开头，右指针 指向结尾
只考虑字母和数字，跳过其他字符
若 s[left] != s[right]，则不是回文
移动指针 left++ 或 right-- 继续比较
"""


def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome_EmptyString_ReturnsTrue(self):
        self.assertTrue(is_palindrome(""))

    def test_is_palindrome_SingleCharacter_ReturnsTrue(self):
        self.assertTrue(is_palindrome("a"))

    def test_is_palindrome_TwoSameCharacters_ReturnsTrue(self):
        self.assertTrue(is_palindrome("aa"))

    def test_is_palindrome_TwoDifferentCharacters_ReturnsFalse(self):
        self.assertFalse(is_palindrome("ab"))

    def test_is_palindrome_PalindromeString_ReturnsTrue(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_is_palindrome_NonPalindromeString_ReturnsFalse(self):
        self.assertFalse(is_palindrome("hello"))

    def test_is_palindrome_PalindromeDifferentCase_ReturnsFalse(self):
        self.assertFalse(is_palindrome("RaceCar"))

    def test_is_palindrome_PalindromeWithNonAlphanumeric_ReturnsFalse(self):
        self.assertFalse(is_palindrome("A man, a plan, a canal, Panama"))


"""
示例2：寻找环的起点
题目：如果链表有环，返回环的起点节点。

思路：

先用快慢指针判断是否有环（如上）。
如果有环，让 其中一个指针回到起点，另一个指针停留在相遇点。
两个指针每次走一步，相遇时即为环的起点。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detect_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # 有环
            return True
    return False


class TestDetectCycle(unittest.TestCase):
    def test_detect_cycle_EmptyList_ReturnsFalse(self):
        self.assertFalse(detect_cycle(None))

    def test_detect_cycle_NoCycle_ReturnsFalse(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        self.assertFalse(detect_cycle(head))

    def test_detect_cycle_CycleExists_ReturnsTrue(self):
        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        head.next = node2
        node2.next = node3
        node3.next = node2  # 创建循环
        self.assertTrue(detect_cycle(head))

    def test_detect_cycle_SingleNodeNoCycle_ReturnsFalse(self):
        head = ListNode(1)
        self.assertFalse(detect_cycle(head))

    def test_detect_cycle_SingleNodeCycle_ReturnsTrue(self):
        head = ListNode(1)
        head.next = head  # 创建自循环
        self.assertTrue(detect_cycle(head))


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
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow  # 返回环的起点
    return None  # 没有环


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TestDetectCycle(unittest.TestCase):
    def test_detect_cycle_EmptyList_ReturnsNone(self):
        self.assertIsNone(detect_cycle(None))

    def test_detect_cycle_NoCycle_ReturnsNone(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        self.assertIsNone(detect_cycle(head))

    def test_detect_cycle_CycleAtBeginning_ReturnsHead(self):
        head = ListNode(1)
        head.next = head
        self.assertIs(detect_cycle(head), head)

    def test_detect_cycle_CycleInMiddle_ReturnsCycleStart(self):
        head = ListNode(1)
        head.next = ListNode(2)
        cycle_start = ListNode(3)
        head.next.next = cycle_start
        cycle_start.next = ListNode(4)
        cycle_start.next.next = cycle_start
        self.assertIs(detect_cycle(head), cycle_start)

    def test_detect_cycle_CycleAtEnd_ReturnsCycleStart(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        cycle_start = ListNode(4)
        head.next.next.next = cycle_start
        cycle_start.next = cycle_start
        self.assertIs(detect_cycle(head), cycle_start)


"""
示例1：最小覆盖子串
题目：给定字符串 s 和 t，在 s 中找到包含 t 所有字符的最小子串。

思路：

用 双指针（滑动窗口） 维护 left 和 right。
右指针扩展窗口，直到窗口包含 t 的所有字符。
左指针收缩窗口，直到不能再缩小为止。
记录最短子串的 start 和 length
"""

if __name__ == '__main__':
    unittest.main()
