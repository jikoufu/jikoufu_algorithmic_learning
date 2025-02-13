from ListNode.linked_list import ListNode


class LinkedListQueue:
    """基于链表实现的队列"""

    def __init__(self):
        """构造方法"""
        self._front: ListNode | None = None  # 头节点 front
        self._rear: ListNode | None = None  # 尾节点 rear
        self._size: int = 0

    def size(self) -> int:
        """获取队列的长度"""
        return self._size

    def is_empty(self) -> bool:
        """判断队列是否为空"""

        return self._size == 0

    def push(self, num: int):
        """入队"""
        # 在尾节点后添加 num
        node = ListNode(num)

        # 判断是否为空队列
        if self.is_empty():
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node

        self._size += 1

    def peek(self) -> int:
        """访问队首元素"""
        if self.is_empty():
            raise IndexError("队列为空")
        return self._front.val

    def pop(self) -> int:
        """出队"""
        num = self.peek()

        self._front = self._front.next
        self._size -= 1
        return num

    def to_list(self) -> list[int]:
        """转化为列表用于打印"""
        queue = []
        temp = self._front
        while temp:
            queue.append(temp.val)
            temp = temp.next
        return queue


que = LinkedListQueue()
# 元素入队
que.push(1)
que.push(3)
que.push(2)
que.push(5)
que.push(4)

# 访问队首元素
front: int = que.peek()
print(front)

# 元素出队
pop: int = que.pop()
print(pop)
# 获取队列的长度
size: int = que.size()
print(size)
# 判断队列是否为空
is_empty: bool = que.is_empty()
print(is_empty)