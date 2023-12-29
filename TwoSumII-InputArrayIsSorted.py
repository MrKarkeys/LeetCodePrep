class Solution(object):
    def twoSum(self, num, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(num)-1
        while (num[left] + num[right] != target):
            if num[left] + num[right] < target:
                left += 1
            else:
                right -= 1
        return [left+1, right+1]
        