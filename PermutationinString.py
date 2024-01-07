class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        maps1 = {}
        maps2 = {}
        matches = 0
        for i in s1:
            maps1[i] = 1 + maps1.get(i, 0)
        left = 0
        for right in range(len(s2)):
            maps2[s2[right]] = 1 + maps2.get(s2[right], 0)
            if maps2[s2[right]] == maps1.get(s2[right], 0):
                matches += 1
            if matches == len(maps1):
                return True
            if (right-left+1 == len(s1)):
                if maps2[s2[left]] == maps1.get(s2[left], 0):
                    matches -= 1
                maps2[s2[left]] -= 1
                left += 1
        return False


        