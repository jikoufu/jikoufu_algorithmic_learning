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
        print(hash_map)

    return []



import unittest


class TestTwoSum(unittest.TestCase):
    def test_two_sum_FoundPair_ReturnsIndices(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        result = two_sum(nums, target)
        self.assertEqual(result, expected)


    def test_two_sum_MultiplePairs_ReturnsFirstPair(self):
        nums = [3, 3, 3, 3]
        target = 6
        expected = [0, 1]
        result = two_sum(nums, target)
        self.assertEqual(result, expected)

    def test_two_sum_SingleElement_ReturnsEmptyList(self):
        nums = [1]
        target = 1
        expected = []
        result = two_sum(nums, target)
        self.assertEqual(result, expected)

    def test_two_sum_EmptyList_ReturnsEmptyList(self):
        nums = []
        target = 1
        expected = []
        result = two_sum(nums, target)
        self.assertEqual(result, expected)

    def test_two_sum_NegativeNumbers_ReturnsIndices(self):
        nums = [-1, -2, -3, -4]
        target = -6
        expected = [1, 3]
        result = two_sum(nums, target)
        self.assertEqual(result, expected)

    def test_two_sum_ZeroTarget_ReturnsIndices(self):
        nums = [0, 0, 1, 2]
        target = 0
        expected = [0, 1]
        result = two_sum(nums, target)
        self.assertEqual(result, expected)

    def test_two_sum_LargeNumbers_ReturnsIndices(self):
        nums = [1000000000, 1000000000]
        target = 2000000000
        expected = [0, 1]
        result = two_sum(nums, target)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
