"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
"""

"""
1. 理解二分法的核心思想
二分法适用于有序数组，通过不断缩小搜索范围来查找目标值，时间复杂度为 O(log n)。

基本逻辑：

设定左右边界 left 和 right。
计算中间索引 mid = left + (right - left) / 2（防止整数溢出）。
比较 nums[mid] 和目标值：
相等：返回 mid，找到目标值。
小于目标值：搜索范围缩小到右半部分 left = mid + 1。
大于目标值：搜索范围缩小到左半部分 right = mid - 1。
直到 left > right，返回 -1（目标值不存在）。
"""


def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(binary_search(nums, target))
