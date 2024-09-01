class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = [""] * (len(s)//k)
        start = 0
        resultcnt = 0
        while start < len(s):
            val = 0
            for i in range(k):
                val += ord(s[start])-ord('a')
                start += 1
            val = val%26
            result[resultcnt] = chr(val+ord('a'))
            resultcnt += 1
        return "".join(result)

