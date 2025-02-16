**反转链表的一部分（Reverse Linked List II）** 是 **反转整个链表的进阶版**，要求 **仅反转从位置 `left` 到 `right` 的子链表**，其余部分保持不变。例如：

---

## **📌 1. 问题描述**
给定单链表 `1 -> 2 -> 3 -> 4 -> 5 -> None`，  
如果 `left = 2, right = 4`，则反转位置 `2` 到 `4` 之间的部分，结果变成：
```
1 -> 4 -> 3 -> 2 -> 5 -> None
```
**要求：**
- 反转 `left` 到 `right` 之间的部分，不影响其他部分。
- **时间复杂度 O(n)，空间复杂度 O(1)**。

---

## **📌 2. 解决思路**
### **(1) 分解问题**
我们把这个链表拆成 **三个部分**：
1. **左侧不变部分**：`head -> ... -> before_left`
2. **需要反转的部分**：`left -> ... -> right`
3. **右侧不变部分**：`right.next -> ... -> None`

然后，我们：
✅ **找到 `left` 之前的节点 (`before_left`)**  
✅ **找到 `right` 节点，并记录 `right.next`**  
✅ **在 `left` 到 `right` 之间进行局部反转**  
✅ **重新连接 `before_left` 和 `right.next`**

---

### **(2) 关键步骤**
**假设链表**：
```
head -> 1 -> 2 -> 3 -> 4 -> 5 -> None
```
我们需要反转 `2 -> 3 -> 4`，让它变成 `4 -> 3 -> 2`。

#### **步骤**
| 步骤 | 变化 | 说明 |
|------|------|------|
| 1 | 找到 `before_left`（即 `1`），并记录 `right.next`（即 `5`） | 为后续拼接做准备 |
| 2 | 反转 `2 -> 3 -> 4` 变成 `4 -> 3 -> 2` | 使用 **双指针法** 反转 |
| 3 | 连接 `before_left.next = 4`，`2.next = 5` | 把反转部分拼接回去 |

最终结果：
```
head -> 1 -> 4 -> 3 -> 2 -> 5 -> None
```

---

## **📌 3. 代码实现**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_between(head, left, right):
    if not head or left == right:
        return head  # 特殊情况：空链表 or 不需要反转

    dummy = ListNode(0)  # 哑节点，方便操作
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
```

---

## **📌 4. 代码解析**
### **(1) 找到 `before_left`**
```python
prev = dummy
for _ in range(left - 1):
    prev = prev.next
before_left = prev
left_node = prev.next
```
- `prev` 初始指向 `dummy`，经过 `left - 1` 次遍历，指向 `left` 之前的节点 (`before_left`)。
- `left_node = prev.next` 是 `left` 位置的节点。

### **(2) 反转 `left -> right`**
```python
prev = None
curr = left_node
for _ in range(right - left + 1):
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node
```
- **双指针反转链表**：
  - `prev` 最终会指向 `right` 位置的节点（新头部）。
  - `curr` 最终会指向 `right.next`。

### **(3) 重新连接**
```python
before_left.next.next = curr  # 让原来的 left 连接 right 之后的部分
before_left.next = prev  # 让 left 之前的部分连接反转后的头部
```
- `before_left.next`（即原来的 `left`）连接 `curr`（即 `right.next`）。
- `before_left.next` 变为 `prev`，即新的反转头部。

---

## **📌 5. 代码执行过程**
假设 `head = [1,2,3,4,5]`，`left = 2`，`right = 4`
```
dummy -> 1 -> 2 -> 3 -> 4 -> 5
              ↑    ↑    ↑
         before_left left right
```
### **找到 `before_left` 和 `left`**
```
before_left = 1
left_node = 2
```
### **反转 `2 -> 3 -> 4`**
```
1 -> 2    3 -> 4 -> 5
1    <- 2    3 -> 4 -> 5
1    <- 2 <- 3    4 -> 5
1    <- 2 <- 3 <- 4    5
```
**结果：**
```
1 -> 4 -> 3 -> 2 -> 5
```

---

## **📌 6. 时间 & 空间复杂度**
| 方法 | 时间复杂度 | 空间复杂度 | 适用情况 |
|------|----------|----------|--------|
| **迭代（双指针）** | O(n) | O(1) | **推荐，适用于大规模数据** |
| **递归**（不推荐） | O(n) | O(n) | **适用于链表较短的情况** |

---

## **📌 7. 递归解法（可选）**
递归方法不如迭代法高效，但逻辑清晰：
```python
def reverse_between_recursive(head, left, right):
    if left == 1:  # 递归基准：当 left == 1 时，直接反转前 right 个元素
        return reverse_first_n(head, right)

    head.next = reverse_between_recursive(head.next, left - 1, right - 1)
    return head

def reverse_first_n(head, n):
    if n == 1:
        return head
    new_head = reverse_first_n(head.next, n - 1)
    head.next.next = head
    head.next = None
    return new_head
```

---

## **📌 8. 总结**
✅ **迭代法是最佳解法，O(n) 时间，O(1) 空间**  
✅ **掌握 `before_left` 定位 + 局部反转 + 重新连接**  
✅ **理解 `prev` 和 `curr` 的指针变换**  
✅ **递归法概念清晰，但不推荐大规模使用**  
