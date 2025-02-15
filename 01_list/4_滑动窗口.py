"""
(1) 无重复字符的最长子串
题目：给定字符串 s，找出不含重复字符的最长子串的长度。
示例：

输入: "abcabcbb"
输出: 3 （最长无重复子串是 "abc"）
思路：

right 右移，将字符加入窗口。
若出现重复字符，则left 右移，直到窗口无重复字符。
过程中记录最长子串的长度。
"""


def length_of_longest_substring(s):
    left = 0
    window = {}
    max_length = 0

    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1

        # 若窗口内有重复字符，则缩小窗口
        while window[char] > 1:
            window[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
