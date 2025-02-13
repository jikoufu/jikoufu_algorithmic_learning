def remove(nums: list[int], index: int):
    """删除索引 index 处的元素"""

    for i in range(index, len(nums) - 1):
        nums[index] = nums[i+1]
