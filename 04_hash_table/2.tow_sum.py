"""
问题：给定一个整数数组 nums 和一个目标值 target，找出数组中两个数的和等于 target 的索引。

思路：
使用哈希表存储数组元素的值及其索引，在遍历数组时，判断当前元素是否存在于哈希表中。

算法：
遍历数组，检查目标值 target - nums[i] 是否在哈希表中。
如果存在，返回当前索引和目标值的对应索引。
否则，将当前元素的值和索引存入哈希表。
"""


def two_sum(nums, target):
    hash_map = {}  # 哈希表存储值及索引
    for i, num in enumerate(nums):
        complement = target - num  # 补数
        if complement in hash_map:
            return [hash_map[complement], i]  # 找到结果
        hash_map[num] = i  # 将当前数值及其索引存入哈希表
    return []
