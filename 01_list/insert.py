def insert(nums: list[int], num: int, index: int):
    """在数组的索引 index 处插入元素 num"""

    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    # 将 num 赋给 index 处的元素
    nums[index] = num
