class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = defaultdict(list)
        for i in strs:
            temp = i
            temp = "".join(sorted(temp))
            map[temp].append(i)
        return map.values()

        