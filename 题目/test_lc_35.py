"""
编号35：搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
"""


def binara_search(sums, target):
    left, right = 0, len(sums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if sums[mid] == target:
            return mid
        elif sums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return right + 1


import unittest


class TestBinaraSearch(unittest.TestCase):
    """二分查找函数单元测试类"""

    def test_target_found_in_middle(self):
        """测试目标值在数组中间位置找到"""
        sums = [1, 3, 5, 6, 8]
        target = 5
        expected = 2
        result = binara_search(sums, target)
        self.assertEqual(result, expected, f"在数组{sums}中查找{target}应该返回索引{expected}")

    def test_target_found_at_beginning(self):
        """测试目标值在数组开头找到"""
        sums = [1, 3, 5, 6, 8]
        target = 1
        expected = 0
        result = binara_search(sums, target)
        self.assertEqual(result, expected, f"在数组{sums}中查找{target}应该返回索引{expected}")

    def test_target_found_at_end(self):
        """测试目标值在数组末尾找到"""
        sums = [1, 3, 5, 6, 8]
        target = 8
        expected = 4
        result = binara_search(sums, target)
        self.assertEqual(result, expected, f"在数组{sums}中查找{target}应该返回索引{expected}")

    def test_target_insert_in_middle(self):
        """测试目标值需要插入到数组中间"""
        sums = [1, 3, 5, 6, 8]
        target = 4
        expected = 2  # 应该插入到索引2的位置
        result = binara_search(sums, target)
        self.assertEqual(result, expected, f"在数组{sums}中查找{target}应该返回插入位置{expected}")

    def test_target_insert_at_beginning(self):
        """测试目标值需要插入到数组开头"""
        sums = [1, 3, 5, 6, 8]
        target = 0
        expected = 0  # 应该插入到索引0的位置
        result = binara_search(sums, target)
        self.assertEqual(result, expected, f"在数组{sums}中查找{target}应该返回插入位置{expected}")

    def test_target_insert_at_end(self):
        """测试目标值需要插入到数组末尾"""
        sums = [1, 3, 5, 6, 8]
        target = 10
        expected = 5  # 应该插入到索引5的位置（数组末尾）
        result = binara_search(sums, target)
        self.assertEqual(result, expected, f"在数组{sums}中查找{target}应该返回插入位置{expected}")

    def test_empty_array(self):
        """测试空数组情况"""
        sums = []
        target = 5
        expected = 0  # 空数组时应该返回0
        result = binara_search(sums, target)
        self.assertEqual(result, expected, f"在空数组中查找{target}应该返回{expected}")

    def test_single_element_array_target_found(self):
        """测试单元素数组且找到目标值"""
        sums = [5]
        target = 5
        expected = 0
        result = binara_search(sums, target)
        self.assertEqual(result, expected, f"在数组{sums}中查找{target}应该返回索引{expected}")

    def test_single_element_array_target_insert_before(self):
        """测试单元素数组且目标值需要插入到前面"""
        sums = [5]
        target = 3
        expected = 0
        result = binara_search(sums, target)
        self.assertEqual(result, expected, f"在数组{sums}中查找{target}应该返回插入位置{expected}")

    def test_single_element_array_target_insert_after(self):
        """测试单元素数组且目标值需要插入到后面"""
        sums = [5]
        target = 7
        expected = 1
        result = binara_search(sums, target)
        self.assertEqual(result, expected, f"在数组{sums}中查找{target}应该返回插入位置{expected}")

    def test_duplicate_elements_target_found_first(self):
        """测试重复元素数组且找到第一个匹配的元素"""
        sums = [1, 2, 2, 2, 5]
        target = 2
        # 二分查找可能返回任意一个匹配位置，这里验证返回值在合理范围内
        result = binara_search(sums, target)
        self.assertIn(result, [1, 2, 3], f"在数组{sums}中查找{target}应该返回1,2,3中的一个索引")

    def test_large_array_performance(self):
        """测试较大数组的性能"""
        sums = list(range(0, 1000, 2))  # [0, 2, 4, 6, ..., 998]
        target = 500
        expected = 250  # 500在索引250位置
        result = binara_search(sums, target)
        self.assertEqual(result, expected, f"在大数组中查找{target}应该返回索引{expected}")


if __name__ == '__main__':
    unittest.main()
