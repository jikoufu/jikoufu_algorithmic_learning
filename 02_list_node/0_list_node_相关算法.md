
链表相关的算法主要分为**基础操作**和**高级技巧**两大类，涉及增删改查、快慢指针、递归、排序等常见考点。  

---

# **📌 1. 基础操作**
基础操作是链表算法的核心，主要包括：
1. **遍历**
2. **插入**
3. **删除**
4. **查找**

### **(1) 遍历链表**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def traverse(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
```
---

### **(2) 插入节点**
**在链表头部插入**
```python
def insert_at_head(head, val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node  # 返回新的头节点
```
**在链表尾部插入**
```python
def insert_at_tail(head, val):
    if not head:
        return ListNode(val)
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = ListNode(val)
    return head
```
---

### **(3) 删除节点**
**删除链表中值为 `val` 的第一个节点**
```python
def delete_node(head, val):
    dummy = ListNode(0)
    dummy.next = head
    prev, curr = dummy, head
    
    while curr:
        if curr.val == val:
            prev.next = curr.next  # 跳过当前节点
            break
        prev, curr = curr, curr.next
    return dummy.next
```
---

### **(4) 查找节点**
**查找链表中值为 `val` 的节点**
```python
def find_node(head, val):
    while head:
        if head.val == val:
            return head
        head = head.next
    return None
```
---

# **📌 2. 进阶算法**
## **(1) 反转链表**
**反转整个链表（双指针迭代法）**
```python
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next  # 保存下一个节点
        curr.next = prev  # 反转指针
        prev = curr  # 移动 prev
        curr = next_node  # 移动 curr
    return prev  # prev 变成新的头节点
```
📌 **时间复杂度 O(n)，空间复杂度 O(1)**

---

## **(2) 反转链表的一部分**
**反转 `m` 到 `n` 位置的链表**
```python
def reverse_between(head, m, n):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # 移动到 m 位置
    for _ in range(m - 1):
        prev = prev.next

    # 反转 m 到 n 之间的节点
    curr = prev.next
    for _ in range(n - m):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next
```
📌 **适用于部分反转，例如 [1,2,3,4,5] 反转 (2,4) 变为 [1,4,3,2,5]**

---

## **(3) 快慢指针**
### **判断链表是否有环**
**思路**：使用**快慢指针**，快指针一次走两步，慢指针一次走一步，如果两者相遇，则有环。
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```
📌 **时间复杂度 O(n)，空间复杂度 O(1)**

---

### **找到链表环的起点**
```python
def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow  # 返回环的起点
    return None
```
📌 **适用于检测环起点，如 LeetCode 142**

---

## **(4) 删除倒数第 `n` 个节点**
**思路**：用**双指针**，先让 `fast` 先走 `n` 步，然后 `slow` 和 `fast` 一起走，直到 `fast` 到达链表末尾，`slow` 指向的就是倒数第 `n` 个节点的前一个节点。
```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy

    for _ in range(n + 1):  # 让 fast 先走 n+1 步
        fast = fast.next
    
    while fast:  # 一起走直到 fast 走到底
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next  # 删除目标节点
    return dummy.next
```
📌 **时间复杂度 O(n)，空间复杂度 O(1)**

---

## **(5) 合并两个有序链表**
```python
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy

    while l1 and l2:
        if l1.val < l2.val:
            curr.next, l1 = l1, l1.next
        else:
            curr.next, l2 = l2, l2.next
        curr = curr.next

    curr.next = l1 if l1 else l2
    return dummy.next
```
📌 **适用于归并排序的合并子问题**

---

## **(6) 归并排序链表**
```python
def sort_list(head):
    if not head or not head.next:
        return head

    # 使用快慢指针找到中点
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None  # 断开链表

    left = sort_list(head)  # 递归排序左半部分
    right = sort_list(mid)  # 递归排序右半部分
    return merge_two_lists(left, right)  # 归并
```
📌 **适用于 O(n log n) 的链表排序**

---

