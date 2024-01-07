class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        letters = {}
        maxcount = 0
        for right in range(len(s)):
            letters[s[right]] = 1 + letters.get(s[right], 0)
            while(right - left + 1 - max(letters.values()) > k):
                letters[s[left]] = letters[s[left]] - 1
                left += 1
            maxcount = max(maxcount, right - left + 1)
        return maxcount
        
        