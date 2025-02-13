"""
示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]

"""
nums = [2, 7, 11, 15]
target = 9


def public_void_add(nums: list, target: int):
    # 遍历列表
    for i in range(len(nums)):
        # 计算需要找到的下一个目标数字
        res = target - nums[i]
        # 遍历剩下的元素，查找是否存在该数字
        if res in nums[i + 1:]:
            # 若存在，返回答案。这里由于是两数之和，可采用.index()方法
            # 获得目标元素在nums[i+1:]这个子数组中的索引后，还需加上i+1才是该元素在nums中的索引
            return [i, nums[i + 1:].index(res) + i + 1]


list = public_void_add(nums, target)
print(list)
