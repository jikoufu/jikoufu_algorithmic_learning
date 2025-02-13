# 初始化栈
# Python 没有内置的栈类，可以把 01_list 当作栈来使用
stack: list[int] = []
# 元素入栈
stack.append(1)
stack.append(3)
stack.append(2)
stack.append(5)
stack.append(4)
# 访问栈顶元素
peek: int = stack[-1]
print("peek",peek)

# 元素出栈
pop: int = stack.pop()
print("pop",pop)
# 获取栈的长度
size: int = len(stack)
print("size",size)
# 判断是否为空
is_empty: bool = len(stack) == 0
print("is_empty",is_empty)

class ArrayStack:
    """基于数组实现的栈"""

    def __init__(self):
        """构造方法"""
        self._stack: list[int] = []

    def size(self) -> int:
        """获取栈的长度"""
        return len(self._stack)

    def is_empty(self) -> bool:
        """判断栈是否为空"""
        return self.size == 0

    def push(self, item: int):
        """入栈"""
        self._stack.append(item)

    def pop(self) -> int:
        """出栈"""
        if self.is_empty():
            raise IndexError("栈为空")
        return self._stack.pop()

    def peek(self) -> int:
        """访问栈顶元素"""
        if self.is_empty():
            raise IndexError("栈为空")
        return self._stack[-1]

    def to_list(self) -> list[int]:
        """返回列表用于打印"""
        return self._stack



