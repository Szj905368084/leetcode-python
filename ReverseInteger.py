

'''
示例 1:
输入: 123
输出: 321
示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #trans_str = str(x)
        if x >= 0:
            trans_str = str(x)
            return int(trans_str[::-1]) if int(trans_str[::-1]) <= 2**31-1 else 0
        else:
            trans_str = str(x)[::-1][:-1]
            return -int(trans_str) if int(trans_str) < 2**31 else 0
