class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxval = 0
        left = 0
        lists = []
        for right in range(len(s)):
            while s[right] in lists:
                lists.remove(s[left])
                left += 1
            maxval = max(maxval, right-left+1)
            lists.append(s[right])
        return maxval


            
        